#!/usr/bin/env python3
"""Minimal TOTP demonstration mirroring openconnect-sso."""

import os
import time

import pyotp


def main() -> None:
    secret = os.environ.get("TOTP_SECRET", "JBSWY3DPEHPK3PXP")
    totp = pyotp.TOTP(secret)

    current_otp = totp.now()
    print(f"Secret (base32): {secret}")
    print(f"Current OTP: {current_otp}")

    print("Verifying immediately:", totp.verify(current_otp))

    later = int(time.time()) + 40
    print(
        "Verifying 40s later with default window:",
        totp.verify(current_otp, for_time=later),
    )
    print(
        "Verifying 40s later allowing drift=1:",
        totp.verify(current_otp, for_time=later, valid_window=1),
    )


if __name__ == "__main__":
    main()
