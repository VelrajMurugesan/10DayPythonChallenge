nameList: list[str] = ["Alice", "Bob", "Charlie", "Diana"]

for i in range(len(nameList)):
   # print(f"Index {i}: {nameList[i]}")

   # print(nameList.pop)

    nameList.remove("Bob")
    print(nameList)
