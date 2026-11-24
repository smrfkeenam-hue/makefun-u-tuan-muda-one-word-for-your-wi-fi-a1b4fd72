import os

# One word for my Wi-Fi: "mirage" — full signal bars, nothing loads.
ENTRY = "mirage"


def write_entry(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    write_entry(out_path)


if __name__ == "__main__":
    main()
