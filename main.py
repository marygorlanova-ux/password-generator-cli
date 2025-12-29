import argparse
from src.generator import generate_password


def main():
    parser = argparse.ArgumentParser(
        description="CLI генератор паролей"
    )

    parser.add_argument(
        "--length", type=int, default=12,
        help="Длина пароля"
    )
    parser.add_argument("--no-lower", action="store_true")
    parser.add_argument("--no-upper", action="store_true")
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--symbols", action="store_true")

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_lower=not args.no_lower,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_symbols=args.symbols
    )

    print(f"Сгенерированный пароль: {password}")


if __name__ == "__main__":
    main()
