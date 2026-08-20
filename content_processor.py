def process_content(content):
    return {
        "processing_status": "Completed",
        "content_available": bool(content)
    }


if __name__ == "__main__":
    sample_content = "Sample agency content for demonstration."

    result = process_content(sample_content)
    print(result)
