from __future__ import division
import itertools
import re
import hashlib

K = 4


def jaccard_set(s1, s2):
    u = s1.union(s2)
    i = s1.intersection(s2)
    return len(i)/len(u)


def make_a_set_of_tokens(doc):
    tokens = re.sub("[^\w]", " ", doc)

    token_set = set()
    for i in range(len(tokens)-K):
        t = tokens[i]
        for x in tokens[i+1:i+K]:
            t += ' ' + x
        token_set.add(t)
    return token_set


if __name__ == '__main__':
    documents = ["The legal system is made up of civil courts, criminal courts and specialty courts such as family law"
                 " courts and bankruptcy court. Each court has its own jurisdiction, which refers to the cases that the"
                 " court is allowed to hear. In some instances, a case can only be heard in one type of court."
                 " For example, a bankruptcy case must be heard in a bankruptcy court. In other instances, there may be"
                 " several potential courts with jurisdiction. For example, a federal criminal court and a state"
                 " criminal court would each have jurisdiction over a crime that is a federal drug offense but that is"
                 " also an offense on the state level.",
                 "The legal system is comprised of criminal and civil courts and specialty courts like bankruptcy and"
                 " family law courts. Every one of the courts is vested with its own jurisdiction. Jurisdiction means"
                 " the types of cases each court is permitted to rule on. Sometimes, only one type of court can hear a"
                 " particular case. For instance, bankruptcy cases an be ruled on only in bankruptcy court. In other"
                 " situations, it is possible for more than one court to have jurisdiction. For instance, both a state"
                 " and federal criminal court could have authority over a criminal case that is illegal under federal"
                 " and state drug laws.",
                 "In many jurisdictions the judicial branch has the power to change laws through the process of"
                 " judicial review. Courts with judicial review power may annul the laws and rules of the state when it"
                 " finds them incompatible with a higher norm, such as primary legislation, the provisions of the"
                 " constitution or international law. Judges constitute a critical force for interpretation and"
                 " implementation of a constitution, thus de facto in common law countries creating the body of"
                 " constitutional law."]

    shingles = []

    print "md5 hash of 'a' in hex is: {}".format(hashlib.md5('a').hexdigest())
    print "...using sha512: {}".format(hashlib.sha512('a').hexdigest())

    for docs in documents:
        sh = make_a_set_of_tokens(docs)
        print "sh = {}".format(sh)

        bucket = map(hash, sh)

        print "bucket = {}".format(bucket)

        shingles.append(set(bucket))

    print "shingles = {}".format(shingles)

    combinations = list(itertools.combinations([y for y in range(len(shingles))], 2))
    print "combinations = {}".format(combinations)

    for c in combinations:
        i1 = c[0]
        i2 = c[1]
        jac = jaccard_set(shingles[i1], shingles[i2])
        print "{} : jacard={}".format(c, jac)
