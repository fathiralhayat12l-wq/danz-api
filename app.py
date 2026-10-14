from flask import Flask, jsonify, request
import random
import os

app = Flask(__name__)

def make_uid(pattern="random"):
    """
    Generates an illustrative numeric ID only.
    It does NOT check whether an ID exists or belongs to a Free Fire account.
    """
    if pattern == "pretty":
        # Repeated-digit style, e.g. 18335555555
        prefix = random.choice(["18", "19"])
        repeated = random.choice("3456789")
        tail = repeated * 6
        middle = "".join(random.choice("0123456789") for _ in range(3))
        return prefix + middle + tail

    if pattern == "1555":
        # Numeric pattern inspired by a 1555-style request; still synthetic.
        return "15" + "".join(random.choice("0123456789") for _ in range(2)) + "555" + "".join(
            random.choice("0123456789") for _ in range(4)
        )

    return str(random.randint(10_000_000, 99_999_999))

@app.get("/")
def home():
    return jsonify({
        "name": "Danz API",
        "status": "online",
        "version": "1.0.0",
        "endpoints": ["/health", "/generate?count=5&pattern=random"],
        "note": "Generated numbers are synthetic; this API does not verify real game accounts."
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "Danz API"})

@app.get("/generate")
def generate():
    pattern = request.args.get("pattern", "random").lower()
    if pattern not in {"random", "pretty", "1555"}:
        return jsonify({
            "status": "error",
            "message": "pattern must be random, pretty, or 1555"
        }), 400

    try:
        count = int(request.args.get("count", "1"))
    except ValueError:
        return jsonify({"status": "error", "message": "count must be an integer"}), 400

    if count < 1 or count > 100:
        return jsonify({"status": "error", "message": "count must be between 1 and 100"}), 400

    results = [make_uid(pattern) for _ in range(count)]
    return jsonify({
        "status": "success",
        "creator": "Danz",
        "pattern": pattern,
        "count": count,
        "results": results,
        "verified": False
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
