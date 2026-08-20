def analyze_content(content):
    return {
        "status": "Content Received",
        "characters": len(content),
        "words": len(content.split())
    }


if __name__ == "__main__":
    sample_content = "Automation helps modern agencies improve their workflows."

    result = analyze_content(sample_content)
    print(result)
