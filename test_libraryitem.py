import video_library as vid


def test_library(capsys):
    library = vid.LibraryItem("John", "Steven", 5)
    assert library.name == "John"
    assert library.director == "Steven"
    assert library.rating == 5

    assert library.info() == f"{library.name} - {library.director} *****"

    assert library.stars() == "*****"

    with capsys.disabled():
        print()
        print(f"tested {library.__class__.__name__} successfully")
