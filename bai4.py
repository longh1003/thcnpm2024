#b4
import json

def load_employees():
    with open("data/em.json", encoding="utf-8") as f:
        return json.load(f)

def display(data):
    for em in data:
        for k, v in em.items():
            if k.__eq__("ma_nv"):
                print(f"Ma nhan vien: {v}")
            elif k.__eq__("ten_nv"):
                print(f"Ten nhan vien: {v}")

if __name__ == "__main__":
    data = load_employees()
    display(data)