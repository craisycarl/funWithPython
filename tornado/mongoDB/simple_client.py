from pymongo import MongoClient, errors, ASCENDING
import datetime
import pprint

from bson.objectid import ObjectId

client = MongoClient()

db = client.test_database
print db

collection = db.test_collection
print collection

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts


def fill_db():
    post_id = posts.insert_one(post).inserted_id
    print post_id
    pprint.pprint(posts.find_one({"_id": post_id}))  # match by id
    # new_posts[1] has a different "shape" than the other posts - there is no "tags" field and
    # we've added a new field, "title". This is what we mean when we say that MongoDB is schema-free.

    new_posts = [{"author": "Mike",
                  "text": "Another post!",
                  "tags": ["bulk", "insert"],
                  "date": datetime.datetime(2009, 11, 12, 11, 14)},
                 {"author": "Brad",
                  "title": "MongoDB is fun",
                  "text": "and pretty easy too!",
                  "date": datetime.datetime(2009, 11, 10, 10, 45)}]

    result = posts.insert_many(new_posts)
    print result.inserted_ids


def get(post_id_var):
    # An ObjectId is not the same as its string representation
    # post_id_as_str = str(post_id)
    # posts.find_one({"_id": post_id_as_str})  # no result

    # A common task in web applications is to get an ObjectId from the request URL and
    # find the matching document. It's necessary in this case to convert the ObjectId
    # from a string before passing it to find_one:

    # The web framework gets post_id from the URL and passes it as a string

    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id_var)})
    return document


def query():
    print db.collection_names(include_system_collections=False)

    pprint.pprint(posts.find_one())  # unique match
    pprint.pprint(posts.find_one({"author": "Mike"}))  # match by name

    pprint.pprint(posts.find_one({"author": "Brad"}))  # no match for this guy

    # Querying for More Than One Document:

    # To get more than a single document as the result of a query we use the find() method.
    # find() returns a Cursor instance, which allows us to iterate over all matching documents.
    # For example, we can iterate over every document in the posts collection.

    for the_post in posts.find():
        pprint.pprint(the_post)

    for the_post in posts.find({"author": "Mike"}):
        pprint.pprint(the_post)

    print posts.count()
    print posts.find({"author": "Mike"}).count()

    d = datetime.datetime(2009, 11, 12, 12)
    for the_post in posts.find({"date": {"$lt": d}}).sort("author"):
        pprint.pprint(the_post)


def add_new_index():
    result = db.profiles.create_index([('user_id', ASCENDING)],
                                      unique=True)
    print sorted(list(db.profiles.index_information()))
    return result


def duplicate_profile_test():
    user_profiles = [{'user_id': 211, 'name': 'Luke'},
                     {'user_id': 212, 'name': 'Ziltoid'}]

    try:
        result1 = db.profiles.insert_many(user_profiles)
        new_profile = {'user_id': 213, 'name': 'Drew'}
        duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
        result2 = db.profiles.insert_one(new_profile)  # This is fine.
        result3 = db.profiles.insert_one(duplicate_profile)
        return result1 | result2 | result3
    except errors.BulkWriteError, e:
        print "Duplicate index in database!", e


if "__main__" in __name__:
    if not posts.find_one():  # Database is empty, fill it up!
        print 'adding some posts to the data base'
        fill_db()
    # add_new_index()
    duplicate_profile_test()
    query()
