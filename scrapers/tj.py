import requests
import json


t = []
for cat in [8, 182, 203, 215]:
    data = {
    "operationName": "SearchProducts",
    "variables":{
        "storeCode": "81",
        "availability": "1",
        "published": "1",
        "categoryId": cat,
        "currentPage": 1,
        "pageSize": 2000
    },
    "query": "query SearchProducts($categoryId: String, $currentPage: Int, $pageSize: Int, $storeCode: String = \"81\", $availability: String = \"1\", $published: String = \"1\") {\n  products(\n    filter: {store_code: {eq: $storeCode}, published: {eq: $published}, availability: {match: $availability}, category_id: {eq: $categoryId}}\n    currentPage: $currentPage\n    pageSize: $pageSize\n  ) {\n    items {\n      sku\n      item_title\n      category_hierarchy {\n        id\n        name\n        __typename\n      }\n      primary_image\n      primary_image_meta {\n        url\n        metadata\n        __typename\n      }\n      sales_size\n      sales_uom_description\n      price_range {\n        minimum_price {\n          final_price {\n            currency\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      retail_price\n      fun_tags\n      item_characteristics\n      __typename\n    }\n    total_count\n    pageInfo: page_info {\n      currentPage: current_page\n      totalPages: total_pages\n      __typename\n    }\n    aggregations {\n      attribute_code\n      label\n      count\n      options {\n        label\n        value\n        count\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'Origin': 'https://www.traderjoes.com'
    }

    r = requests.post('https://www.traderjoes.com/api/graphql', json=data, headers=headers)
    data = r.json()['data']['products']['items']
    t.extend(data)
    with open('data/tj.json', 'w') as file:
        json.dump(t, file)

    