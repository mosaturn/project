import cs50youtube

def main():
    assert test_length() == "0:04:17"
    assert test_author() == "CS50"
    assert test_title() == "CS50P - Introduction"

def test_length():
    url = "https://www.youtube.com/watch?v=_eo8l7HP-9U"
    return cs50youtube.length(url)

def test_author():
    url = "https://www.youtube.com/watch?v=_eo8l7HP-9U"
    return cs50youtube.author(url)

def test_title():
    url = "https://www.youtube.com/watch?v=_eo8l7HP-9U"
    return cs50youtube.title(url)

if __name__ == "__main__":
    main()
