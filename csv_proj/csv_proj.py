import research


def main():
    research.init()

    print("Applicant Research")
    print()
    print("The top cities.")
    top_cities = research.top_cities(4)
    print(top_cities)


    print("The top companies.")
    top_companies = research.top_companies(3)
    print(top_companies)


if __name__ == '__main__':
    main()