import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

Cond = input("請輸入課程關鍵字:")

collection_ref = db.collection("111")
docs = collection_ref.get()
for doc in docs:
	result = doc.to_dict()
	if Cond in result["Course"]:
		print("課程為 : " + result["Course"])
		print("老師為 : " + result["Leacture"])
		print("教室為 : " + result["Room"])
		print("時間為 : " + result["Time"])
