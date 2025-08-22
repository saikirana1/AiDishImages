from queue import Queue
import threading
from .openai_client import openai_client
import uuid

task_queue = Queue()

client = openai_client()


def generate_image(prompt: str, data_list: list[str], tworkers: int) -> list[dict]:
    results = []

    if tworkers <= 0:
        raise ValueError(f"{tworkers} tworkers must be greater than zero")

    for dish in data_list:
        task_queue.put(dish)

    def worker():
        while not task_queue.empty():
            try:
                dish = task_queue.get(timeout=1)
            except:
                break

            try:
                print("i am genarating image")
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=f"{prompt} - {dish}",
                    size="1024x1024",
                    quality="standard",
                    n=1,
                    response_format="b64_json",
                )

                base64_image = response.data[0].b64_json
                results.append(
                    {
                        "id": str(uuid.uuid4()),
                        "dish": dish,
                        "image_base64": base64_image,
                    }
                )
            finally:
                task_queue.task_done()

    threads = []
    for i in range(tworkers):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    task_queue.join()

    for thread in threads:
        thread.join()

    return results
