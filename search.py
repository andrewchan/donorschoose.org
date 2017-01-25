#!/usr/bin/env python

import sys
import requests

baseUrl = 'https://api.donorschoose.org/common/json_feed.html'
apiKey = 'DONORSCHOOSE'
maxResult = 5
state = 'CA'
minCost = 0
maxCost = 2000
sortBy = 0
keywords = ''

def search(keyword):
    params = {
        'keywords': keywords,
        'state': state,
        'costToCompleteRange': '%s TO %s' % (minCost, maxCost),
        'sortBy': sortBy,
        'max': maxResult,
        'APIKey': apiKey
    }

    r = requests.get(baseUrl, params=params)
    if r.status_code != 200:
        sys.exit('API call failed; HTTP status code %s returned' % str(r.status_code))

    return r.json()['proposals'] if 'proposals' in r.json() else {}

def printProposal(proposal):
    print('Title: %s' % (proposal['title'] if 'title' in  proposal else 'None'))
    print('Short Description: %s' % (proposal['shortDescription'] if 'shortDescription' in proposal else 'None'))
    print('ProposalURL: %s' % (proposal['proposalURL'] if 'proposalURL' in proposal else 'None'))
    print('Cost To Complete: %s' % (proposal['costToComplete'] if 'costToComplete' in proposal else 'None'))

def getAvg(item, proposals):
    count = 0
    sum = 0

    if proposals:
        for p in proposals:
            if item in p:
                count += 1
                sum += float(p[item])

        return sum / count
    else:
        return 0

def printAvgPercFunded(proposals):
    print('Average Percent Funded: %s' % str(getAvg('percentFunded', proposals)))

def printAvgNumOfDonors(proposals):
    print('Average Number of Donors: %s' % str(getAvg('numDonors', proposals)))

def printAvgCostToComplete(proposals):
    print('Average Cost To Complete: %s' % str(getAvg('costToComplete', proposals)))

def printAvgNumOfStudents(proposals):
    print('Average Number of Students: %s' % str(getAvg('numStudents', proposals)))

def printAvgTotalPrice(proposals):
    print('Average Total Price: %s' % str(getAvg('totalPrice', proposals)))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s <keywords>' % sys.argv[0])
        sys.exit()
    keywords = sys.argv[1].strip()
    proposals = search(keywords)
    for p in proposals:
        printProposal(p)
        print

    printAvgPercFunded(proposals)
    printAvgNumOfDonors(proposals)
    printAvgCostToComplete(proposals)
    printAvgNumOfStudents(proposals)
    printAvgTotalPrice(proposals)