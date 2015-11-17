# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:47:48 2015

@author: ruhansa
"""
import json
# if you are using python 3, you should 
import urllib.request 
from urllib import parse
import os
import subprocess
#import urllib2


# change the url according to your own koding username and query
#inurl = 'http://anudeep3998.koding.io:8983/solr/vsm/select?q=%D0%A0%D0%A4+%D0%B2+%D0%A1%D0%B8%D1%80%D0%B8%D0%B8+%D0%B2%D1%8B%D0%BD%D1%83%D0%B4%D0%B8%D0%BB%D0%B8+250+%D1%82%D1%83%D0%BD%D0%B8%D1%81%D1%81%D0%BA%D0%B8%D1%85+%D0%B1%D0%BE%D0%B5%D0%B2%D0%B8%D0%BA%D0%BE%D0%B2+%D0%B1%D0%B5%D0%B6%D0%B0%D1%82%D1%8C%0A&wt=json&indent=true&defType=dismax&qf=text_ru&fl=id%2Cscore&wt=json&indent=true&rows=1000'
outfn = 'result.txt'

queries = []

'''
clear and reindex
res = os.popen('/home/anudeep3998/cse535/solr/solr-5.3.0/bin/solr restart -s /home/anudeep3998/cse535/solr/solr-5.3.0/projB/solr/')
print( res.read())
urllib.request.urlopen('http://localhost:8983/solr/vsm/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true')
res = os.popen("curl 'http://localhost:8983/solr/vsm/update/json?commit=true' --data-binary @$(echo /home/anudeep3998/cse535/code/projB/train.json) -H 'Content-type:application'")
'''


infn = "/home/anudeep3998/cse535/code/projB/queries.txt"
q_count = 0


#bm : 
#custom_params = "qf=text_dump^1+tweet_hashtags^0.9&mm=1&pf=text_dump"
#lm : 
#custom_params = "qf=text_en^1+text_ru^0.8+text_de^1+tweet_hashtags^0.6&mm=1&pf=text_dump"
#vsm : 
custom_params = "qf=text_en^1.2+text_ru^1+text_de^1+tweet_hashtags^0.5&mm=1&pf=text_dump"



similarity = "vsm"

logger_f = similarity+'/logger.txt'

with open(infn,"r",encoding="utf-8") as inf :
    for line in inf :
        s = "http://anudeep3998.koding.io:8983/solr/"
        s += similarity
        s += "/select?q="
        s += parse.quote_plus(line[4:])
        s += "&fl=id%2Cscore&wt=json&rows=1000&indent=true&defType=dismax&"
        s += custom_params
        queries.append(s)
        q_count += 1


#tuple = ('http://anudeep3998.koding.io:8983/solr/vsm/select?q=Russia%27s+intervention+in+Syria&fl=id%2Cscore&wt=json&indent=true&defType=dismax&qf=text_en+text_ru+text_de+tweet_hashtags&mm=1&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=US+air+dropped+50+tons+of+Ammo+on+Syria%0A&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=The+European+Refugee+Crisis+and+Syria+Explained+animation%0A&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=Wegen+Fl%C3%BCchtlingskrise%3A+Angela+Merkel+st%C3%BCrzt+in+Umfragen%0A&wt=json&indent=true&defType=dismax&qf=text_de&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=%D0%A0%D0%A4+%D0%B2+%D0%A1%D0%B8%D1%80%D0%B8%D0%B8+%D0%B2%D1%8B%D0%BD%D1%83%D0%B4%D0%B8%D0%BB%D0%B8+250+%D1%82%D1%83%D0%BD%D0%B8%D1%81%D1%81%D0%BA%D0%B8%D1%85+%D0%B1%D0%BE%D0%B5%D0%B2%D0%B8%D0%BA%D0%BE%D0%B2+%D0%B1%D0%B5%D0%B6%D0%B0%D1%82%D1%8C%0A&wt=json&indent=true&defType=dismax&qf=text_ru&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=ISIS+Kills+TOP+Iranian+General+in+Syria%0A&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=David+Cameron+urged+to+ensure+vulnerable+Syrian+refugees+are+settled+by+winter%0A&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=RT+%40Free_Media_Hub%0A&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=%23Hezbollah&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=%23Syria+%23SALMA+%23LATAKIA&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=Greek+AFP+photojournalist+Aris+Messinis&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=ASYL-FL%C3%9CCHTLING+bedankt+sich+per+Video-Botschaft+bei+Til+Schweiger%0A013+Airbnb%2C+Instacart%2C+Kickstarter+%0A%0Alaunch+campaigns+to+fund+refugee+relief&wt=json&indent=true&defType=dismax&qf=text_de&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=Airbnb%2C+Instacart%2C+Kickstarter+launch+campaigns+to+fund+refugee+relief%0A%0A&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000','http://anudeep3998.koding.io:8983/solr/vsm/select?q=12-year-old+%23Palestinian+boy+has+died%0A&wt=json&indent=true&defType=dismax&qf=text_en&fl=id%2Cscore&wt=json&indent=true&rows=1000')
res = subprocess.call('rm '+outfn, shell=True)

for i in range(0,q_count):
    # change query id and IRModel name accordingly
    if i<9:
        qid = '00'+ str(i+1)
    else:
        qid = '0'+ str(i+1)
        
    #outfn = similarity+"/"+str(i+1)+".txt"
    with open(outfn, 'a+') as outf : 
            
        IRModel='default'
        #IRModel='BM25Similarity'
        #IRModel='LMJelinekMercerSimilarity'
        #data = urllib2.urlopen(tuple[i])
        # if you're using python 3, you should use
        #print(queries[i])
    
        with urllib.request.urlopen(queries[i]) as data :
            data = data.read().decode('utf-8')
            docs = json.loads(data)['response']['docs']
            # the ranking should start from 1 and increase
            rank = 1
            for doc in docs:
                outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
                rank += 1
                #qid += 1
    
        outf.close()
    #outf.close()

result_file = 'result.txt'
trec_file = 'result_trec_new'
old_file = 'result_trec_old'
analyzed_file = 'result_analyzed_new'
exts = ['','_map','_ndcg','_bpref','_F']

trec_file += '_'+similarity

res = subprocess.call('trec_eval -q -c -M 1000 ../qrel.txt ' + result_file + ' > ' + trec_file + '.txt', shell=True)
res = subprocess.call('trec_eval -q -c -M 1000 -m map ../qrel.txt ' + result_file + ' > ' + trec_file + '_map.txt', shell=True)
res = subprocess.call('trec_eval -q -c -M 1000 -m ndcg ../qrel.txt ' + result_file + ' > ' + trec_file + '_ndcg.txt', shell=True)
res = subprocess.call('trec_eval -q -c -M 1000 -m bpref ../qrel.txt ' + result_file + ' > ' + trec_file + '_bpref.txt', shell=True)
res = subprocess.call('trec_eval -q -c -M 1000 -m set_F.0.5 ../qrel.txt ' + result_file + ' > ' + trec_file + '_F.txt', shell=True)

total_d = []
rel_d = []
ret_rel_d = []
rec_prec_d = []
map_d = []
ndcg_d = []
bpref_d = []
set_f_d = []


with open(old_file+exts[0]+".txt","r",encoding="utf-8") as old:
    for line in old:
        s = line.split()
        if s[0] == 'num_ret' and s[1] == 'all' :
            total_d.append(int(s[2]))
        if s[0] == 'num_rel' and s[1] == 'all' :
            rel_d.append(int(s[2]))
        if s[0] == 'num_rel_ret' and s[1] == 'all' :
            ret_rel_d.append(int(s[2]))
        if s[0] == 'Rprec' and s[1] == 'all' :
            rec_prec_d.append(float(s[2]))
            
with open(trec_file+exts[0]+".txt","r",encoding="utf-8") as old:
    for line in old:
        s = line.split()
        if s[0] == 'num_ret' and s[1] == 'all' :
            total_d.append(int(s[2]))
        if s[0] == 'num_rel' and s[1] == 'all' :
            rel_d.append(int(s[2]))
        if s[0] == 'num_rel_ret' and s[1] == 'all' :
            ret_rel_d.append(int(s[2]))
        if s[0] == 'Rprec' and s[1] == 'all' :
            rec_prec_d.append(float(s[2]))

for i in range(1,5):
    with open(old_file+exts[i]+".txt","r",encoding="utf-8") as old:
        for line in old:
            s = line.split()
            if s[0] == 'map' and s[1] == 'all' :
                map_d.append(float(s[2]))
            if s[0] == 'ndcg' and s[1] == 'all' :
                ndcg_d.append(float(s[2]))
            if s[0] == 'bpref' and s[1] == 'all' :
                bpref_d.append(float(s[2]))
            if s[0] == 'set_F_0.5' and s[1] == 'all' :
                set_f_d.append(float(s[2]))
    
    with open(trec_file+exts[i]+".txt","r",encoding="utf-8") as old:
        for line in old:
            s = line.split()
            if s[0] == 'map' and s[1] == 'all' :
                map_d.append(float(s[2]))
            if s[0] == 'ndcg' and s[1] == 'all' :
                ndcg_d.append(float(s[2]))
            if s[0] == 'bpref' and s[1] == 'all' :
                bpref_d.append(float(s[2]))
            if s[0] == 'set_F_0.5' and s[1] == 'all' :
                set_f_d.append(float(s[2]))
 
 
print('Query params : '+ custom_params)
print('Total docs :\t' + str(total_d[0]) +'\t'+ str(total_d[1]) +'\t'+ str(total_d[1]-total_d[0])+'\n')
print('Rel docs :\t' + str(rel_d[0]) +'\t'+ str(rel_d[1]) +'\t'+ str(rel_d[1]-rel_d[0])+'\n')
print('Rel_Rev docs :\t' + str(ret_rel_d[0]) +'\t'+ str(ret_rel_d[1]) +'\t'+ str(ret_rel_d[1]-ret_rel_d[0])+'\n')
print('RPrec docs :\t' + str(rec_prec_d[0]) +'\t'+ str(rec_prec_d[1]) +'\t'+ str(rec_prec_d[1]-rec_prec_d[0])+'\n')
print('Map score :\t' + str(map_d[0]) +'\t'+ str(map_d[1]) +'\t'+ str(map_d[1]-map_d[0])+'\n')
print('NDCG score :\t' + str(ndcg_d[0]) +'\t'+ str(ndcg_d[1]) +'\t'+ str(ndcg_d[1]-ndcg_d[0])+'\n')
print('BPref score :\t' + str(bpref_d[0]) +'\t'+ str(bpref_d[1]) +'\t'+ str(bpref_d[1]-bpref_d[0])+'\n')
print('F 0.5 score :\t' + str(set_f_d[0]) +'\t'+ str(set_f_d[1]) +'\t'+ str(set_f_d[1]-set_f_d[0])+'\n')

with open(logger_f,"a+",encoding="utf-8") as old:
    old.write('\n')
    old.write('Query params : '+ custom_params+'\n')
    old.write('Index similarity : '+ similarity+'\n')
    old.write('Total docs :\t' + str(total_d[0]) +'\t'+ str(total_d[1]) +'\t'+ str(total_d[1]-total_d[0])+'\n')
    old.write('Rel docs :\t' + str(rel_d[0]) +'\t'+ str(rel_d[1]) +'\t'+ str(rel_d[1]-rel_d[0])+'\n')
    old.write('Rel_Rev docs :\t' + str(ret_rel_d[0]) +'\t'+ str(ret_rel_d[1]) +'\t'+ str(ret_rel_d[1]-ret_rel_d[0])+'\n')
    old.write('RPrec docs :\t' + str(rec_prec_d[0]) +'\t'+ str(rec_prec_d[1]) +'\t'+ str(rec_prec_d[1]-rec_prec_d[0])+'\n')
    old.write('Map score :\t' + str(map_d[0]) +'\t'+ str(map_d[1]) +'\t'+ str(map_d[1]-map_d[0])+'\n')
    old.write('NDCG score :\t' + str(ndcg_d[0]) +'\t'+ str(ndcg_d[1]) +'\t'+ str(ndcg_d[1]-ndcg_d[0])+'\n')
    old.write('BPref score :\t' + str(bpref_d[0]) +'\t'+ str(bpref_d[1]) +'\t'+ str(bpref_d[1]-bpref_d[0])+'\n')
    old.write('F 0.5 score :\t' + str(set_f_d[0]) +'\t'+ str(set_f_d[1]) +'\t'+ str(set_f_d[1]-set_f_d[0])+'\n')