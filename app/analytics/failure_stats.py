def build_failure_stats(jobs: list):

    failures = [j for j in jobs if j.get("status") == "failed"]

    return {
        "total_failures": len(failures),
        "failed_jobs": failures
    }