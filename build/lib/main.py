import click
import textrank
from bs4 import BeautifulSoup
import urllib.request as urllib2
import xlwt
from pythonrouge.pythonrouge import Pythonrouge


@click.group()
def cli():
    pass


@cli.command()
def initialize():
    """Download required nltk libraries."""
    textrank.setup_environment()


# @cli.command()
# @click.argument('filename')
# def extract_summary(filename):
#     """Print summary text to stdout."""
#     with open(filename) as f:
#         summary = textrank.extract_sentences(f.read())
#         print(summary)





# @cli.command()
# @click.argument('filename')
# def extract_phrases(filename):
#     """Print key-phrases to stdout."""
#     with open(filename) as f:
#         phrases = textrank.extract_key_phrases(f.read())
#         print(phrases)

@cli.command()
def get_hindustan_data():
    url = input("Enter a URL:")
    request = urllib2.Request(url)
    result = urllib2.urlopen(request)
    soup = BeautifulSoup(result.read(),'html.parser')
    prop_add = soup.find('div',{'class':'story-details'})
    p = prop_add.text
    f = open('t1.txt','w+')
    f.write("{}".format(p),file=text_file)
    f.close()
    with open(t1.txt) as g:
        phrases = textrank.extract_key_phrases(p)
        summaryV = textrank.extract_sentences(p)
        print("Summary:\n")
        print(summaryV)
        print("phrases:\n")
        print(phrases)


    # python rouge

    # summary = [[summaryV]]
    # reference = [[[p]]]
    # rouge = Pythonrouge(summary_file_exist=False,
    #                 summary=summary, reference=reference,
    #                 n_gram=2, ROUGE_SU4=True, ROUGE_L=False,
    #                 recall_only=True, stemming=True, stopwords=True,
    #                 word_level=True, length_limit=True, length=50,
    #                 use_cf=False, cf=95, scoring_formula='average',
    #                 resampling=True, samples=1000, favor=True, p=0.5)
    # score = rouge.calc_score()
    # print(score)

    # end of python rouge

    # https://www.hindustantimes.com/cricket/ipl-2018-kings-xi-punjab-opt-to-field-against-rajasthan-royals/story-YNTBK4KDp06lhws2nQK8PI.html

@cli.command()
def get_huffington_data():
    url2 = input("Enter a URL:")
    request2 = urllib2.Request(url2)
    result2 = urllib2.urlopen(request2)
    soup2 = BeautifulSoup(result2.read(),'html.parser')
    prop_add2 = soup2.find("div", {"class": "post-contents yr-entry-text"})
    p2 = prop_add2.text
    phrases2 = textrank.extract_key_phrases(p2)
    summaryV2 = textrank.extract_sentences(p2)
    print("Summary:\n")
    print(summaryV2)
    print("phrases:\n")
    print(phrases2)


    # python rouge

    # summary = [[summaryV2]]
    # reference = [[[p2]]]
    # rouge = Pythonrouge(summary_file_exist=False,
    #                 summary=summary, reference=reference,
    #                 n_gram=2, ROUGE_SU4=True, ROUGE_L=False,
    #                 recall_only=True, stemming=True, stopwords=True,
    #                 word_level=True, length_limit=True, length=50,
    #                 use_cf=False, cf=95, scoring_formula='average',
    #                 resampling=True, samples=1000, favor=True, p=0.5)
    # score = rouge.calc_score()
    # print(score)

    # end of python rouge

    # https://www.huffingtonpost.in/2018/05/06/indian-techi-srinivas-kuchibhotlas-killer-gets-life-term_a_23428003/?utm_hp_ref=in-homepage

@cli.command()
def get_toi_data():
    url3 = input("Enter a URL:")
    request3 = urllib2.Request(url3)
    result3 = urllib2.urlopen(request3)
    soup3 = BeautifulSoup(result3.read(),'html.parser')
    prop_add3 = soup3.find('div',{'class' :'Normal'})
    p3 = prop_add3.text
    phrases3 = textrank.extract_key_phrases(p3)
    summaryV3 = textrank.extract_sentences(p3)
    print("Summary:\n")
    print(summaryV3)
    print("phrases:\n")
    print(phrases3)


    # python rouge

    # summary = [[summaryV3]]
    # reference = [[[p3]]]
    # rouge = Pythonrouge(summary_file_exist=False,
    #                 summary=summary, reference=reference,
    #                 n_gram=2, ROUGE_SU4=True, ROUGE_L=False,
    #                 recall_only=True, stemming=True, stopwords=True,
    #                 word_level=True, length_limit=True, length=50,
    #                 use_cf=False, cf=95, scoring_formula='average',
    #                 resampling=True, samples=1000, favor=True, p=0.5)
    # score = rouge.calc_score()
    # print(score)

    # end of python rouge

    # https://timesofindia.indiatimes.com/india/karnataka-assembly-elections-2018-who-said-what/articleshow/64050664.cms
    
