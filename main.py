import eleven_test
import gtts_test
import gcloud_test
import os
from time import perf_counter


def get_tts_fn(service_name: str):
    fn_map = {"gTTS": gtts_test.get_tts,
              "ElevenLabs": eleven_test.get_tts,
              "GoogleCloud": gcloud_test.get_tts}
    return fn_map.get(service_name, None)


def run_tts_perf_test(service: str, strings: list[str]):
    tts = get_tts_fn(service)
    if tts is None or strings == []:
        return

    folder = os.path.join("results", service)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, "test_log.txt")

    times = {}
    for idx, string in enumerate(strings):
        start_time = perf_counter()
        tts(folder, string, str(idx))
        end_time = perf_counter()
        times[idx] = end_time - start_time

    avg_time_pc = sum(times.values()) / sum(map(lambda n: len(n), strings))

    with open(filepath, "w") as file:
        for k, v in times.items():
            file.write(f"Audio for string \"{strings[k]}\"\n-Generated in {v:0.4f} seconds.\n")
            pc_time = v / len(strings[k])
            file.write(f"-Time per character: {pc_time:0.4f} seconds\n")
        file.write(f"\n--Overall Average Time Per Character: {avg_time_pc:0.4f} seconds.\n")


if __name__ == '__main__':
    test_strings = ["The quick brown fox jumped over the lazy dog.",
                    "Puh-koo-zee-mah-flee-dee-oh-blah-gorilla-cabbage-potato.",
                    "The red balloon floated high into the sky as children laughed and played below.",
                    "Qwertyuiopasdfghjklzxcvbnm, 1234567890!",
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."]
    test_service = "GoogleCloud"

    run_tts_perf_test(service=test_service, strings=test_strings)
