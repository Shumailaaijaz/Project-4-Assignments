import os

def main():
    i = 0
    path = "D:/Pictures/"

    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            my_source = os.path.join(path, filename)
            my_dest = os.path.join(path, f"img{i}.jpg")
            os.rename(my_source, my_dest)
            i += 1

if __name__ == "__main__":
    main()

            