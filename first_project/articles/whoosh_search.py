from whoosh.qparser import QueryParser,MultifieldParser
from whoosh import query
import whoosh.index as index
import pickle
import os
parent_dir=os.getcwd()
# ix = index.open_dir("/Users/xujiahui/Downloads/ocbang/bytedance database/recent experience index")
ix = index.open_dir(parent_dir+'/articles/recent experience index')
<<<<<<< HEAD
def load_obj(name ):
    # with open('/Users/xujiahui/Downloads/ocbang/data/' + name + '.pkl', 'rb') as f:
    with open(parent_dir+'/' + name + '.pkl', 'rb') as f:    
=======
# ix = index.open_dir("/Users/xujiahui/Downloads/ocbang/bytedance database/recent experience index")

def load_obj(name ):
#     with open('/Users/xujiahui/Downloads/ocbang/data/' + name + '.pkl', 'rb') as f:
    with open(parent_dir+'/' + name + '.pkl', 'rb') as f: 
>>>>>>> 5e91e2e7789c29d7c3d1371730ab70761b0b10f8
        return pickle.load(f)

structured_profiles=load_obj('bytedance_dictionary_with_loc_renamed')


initiate=[p['id'] for p in structured_profiles]
def content_search(content_keyword):
    mparser = MultifieldParser(["content", "applied_position"], schema=ix.schema)
    res_id=[]
    with ix.searcher() as searcher:
        query = mparser.parse(content_keyword) ## exclusive 9 and 11
    #     query = mparser.parse("work_experience:[9 to 11]")
    #     query1=locationParser('los angeles')
    #     results = searcher.search(query,sortedby=sorting.FieldFacet('work_experience', reverse=True))
        results = searcher.search(query,limit=None)
        for result in results:
            res_id.append(result['id'])
            # print(result['id'],result['applied_position_d'],result['work_experience'])
        return(res_id)
def applied_position_search(position_keyword):
    query = QueryParser("applied_position", ix.schema).parse(position_keyword)
    res_id=[]
    with ix.searcher() as searcher:
#     results = searcher.search(query,sortedby=sorting.FieldFacet('work_experience', reverse=True))
        results = searcher.search(query,limit=None)
        for result in results:
            res_id.append(result['id'])
            # print(result['id'],result['applied_position_d'],result['work_experience'])
        return(res_id)

def location_search(location_keyword):
    query = QueryParser("compound_location", ix.schema).parse(location_keyword)
    res_id=[]
    with ix.searcher() as searcher:
#     results = searcher.search(query,sortedby=sorting.FieldFacet('work_experience', reverse=True))
        results = searcher.search(query,limit=None)
        for result in results:
            res_id.append(result['id'])
            # print(result['id'],result['applied_position_d'],result['work_experience'])
        return(res_id)

def recent_experience_search(recent_keyword):
    query = QueryParser("recent_experience", ix.schema).parse(recent_keyword)
    res_id=[]
    with ix.searcher() as searcher:
#     results = searcher.search(query,sortedby=sorting.FieldFacet('work_experience', reverse=True))
        results = searcher.search(query,limit=None)
        for result in results:
            res_id.append(result['id'])
            # print(result['id'],result['applied_position_d'],result['work_experience'])
        return(res_id)

def company_search(company):
    query = QueryParser("companys", ix.schema).parse(company)
    res_id=[]
    with ix.searcher() as searcher:
#     results = searcher.search(query,sortedby=sorting.FieldFacet('work_experience', reverse=True))
        results = searcher.search(query,limit=None)
        for result in results:
            res_id.append(result['id'])
            # print(result['id'],result['applied_position_d'],result['work_experience'])
        return(res_id)

def title_search(title):
    query = QueryParser("titles", ix.schema).parse(title)
    res_id=[]
    with ix.searcher() as searcher:
#     results = searcher.search(query,sortedby=sorting.FieldFacet('work_experience', reverse=True))
        results = searcher.search(query,limit=None)
        for result in results:
            res_id.append(result['id'])
            # print(result['id'],result['applied_position_d'],result['work_experience'])
        return(res_id)

def search():
    content_res=initiate
    applied_position_res=initiate
    location_res=initiate
    recent_res=initiate
    company_res=initiate
    title_res=initiate
    
    if content_widget.value!='':
        content_res=content_search(content_widget.value)
    
    if applied_position_widget.value!='':
        applied_position_res=applied_position_search(applied_position_widget.value)
    if location_widget.value!='':
        location_res=location_search(location_widget.value)
    if recent_experience_widget.value!='':
        recent_res=recent_experience_search(recent_experience_widget.value)
    if companies_widget.value!='':
        company_res=company_search(companies_widget.value)
    if titles_widget.value!='':
        title_res=title_search(titles_widget.value)
    
    final_result=list(set(content_res).intersection(set(applied_position_res)).intersection(set(location_res)).intersection(set(recent_res)).intersection(set(company_res)).intersection(set(title_res)))
    return(final_result)
def store_results(res_id):
    filtered_profiles=[p for p in structured_profiles if p['id'] in res_id]
    return(filtered_profiles)
