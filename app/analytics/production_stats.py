def build_production_stats(jobs: list):

    total = len(jobs)

    success = len([j for j in jobs if j.get("status") == "success"])

    failed = len([j for j in jobs if j.get("status") == "failed"])

    return {
        "total_jobs": total,
        "success_jobs": success,
        "failed_jobs": failed
    }