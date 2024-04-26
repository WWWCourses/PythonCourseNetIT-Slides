import json

def rearange_books_by_category(books_json):
  """rearange_books_by_category.
    Returns JSON with following structure:
      {
        "Beginner":[
          {
            "title":
            "author":
            "url"
          }
        ],
        "Intermediate":[
          {
            "title":
            "author":
            "url"
          }
        ],
      }
  """
  rearanged_books = {}

  #####################################
  # YOUR CODE IS HERE                 #
  #####################################

  return rearanged_books


def main():
  json_file = "pythonbooks.revolunet.com.issues.json"

  #read json data from file
  with open(json_file) as f:
      json_data = json.load(f)

  rearanged_books = rearange_books_by_category(json_data)

  # print json data:
  print(json.dumps(rearanged_books,indent=4,sort_keys=True))

if __name__ == '__main__':
  main()

