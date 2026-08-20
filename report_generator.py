def generate_report(data):
    return {
        "report_status": "Generated",
        "results": data
    }


if __name__ == "__main__":
    sample_data = {
        "analysis": "Completed",
        "processing": "Completed"
    }

    report = generate_report(sample_data)
    print(report)
