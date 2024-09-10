def process_response(r, allowed_codes=None):
    if not allowed_codes:
        allowed_codes = []

    if not r.ok:
        message = f'{r.status_code}: {r.text if r.text else "Unknown error"} when running {r.request.method} {r.url}'

        if r.status_code in allowed_codes:
            print(f"WARNING: {message}")
        else:
            raise SystemExit(f"ERROR {message}")

    return r.json() if r.content else None
