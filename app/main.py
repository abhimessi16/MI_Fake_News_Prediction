import pickle

from fastapi import FastAPI
from sklearn.feature_extraction.text import TfidfVectorizer

from app.routes.fake_news_predict_route import fake_news_predict_router
from app.params import fake_news_model, vectorization

with open(fake_news_model, "rb") as f:
    model = pickle.load(f)

with open(vectorization, "rb") as f:
    vectorization = pickle.load(f)

fake_news_prediction_app = FastAPI()
fake_news_prediction_app.include_router(fake_news_predict_router)

news = """Spending plan to prevent a government shutdown includes “a pay increase for members of Congress from $174,000 to $243,000 per year.”Business executives Elon Musk and Vivek Ramaswamy, co-leaders of the Department of Government Efficiency, an incoming advisory committee, came out with a host of reasons that Congress should ditch a plan to fund the government and avoid a government shutdown by Dec. 21. Their concerns made it to President-elect Donald Trump, who then announced his opposition to the continuing resolution, making its passage unlikely.  On X, Musk — who declared the bill "dead" — urged lawmakers to vote against the continuing resolution. Similarly, Ramaswamy said he read the approximately 1,500-page bill and described it as "full of excessive spending" and said it "should fail."   The committee, which calls itself DOGE for short, on X also criticized the continuing resolution for, among other things, purportedly including "a pay increase for members of Congress from $174,000 to $243,000 per year."   Lawmaker pay increases are politically contentious, and PolitiFact frequently fact-checks inaccurate claims about congressional compensation changes.  Congress hasn’t increased its pay since 2009, so the idea that it would propose nearly $70,000 raises in stopgap legislation caught our attention. We found that the Department of Government Efficiency’s claim inflated the proposed raises by more than $60,000. The continuing resolution would raise most lawmakers’ salaries by about $6,600.   We messaged the DOGE X account to ask for evidence that the bill included a $69,000 raise for lawmakers and to ask who writes the account’s X posts. We received no response before publication.   (Screenshot from X) For 15 years, lawmakers have blocked pay raises  If passed as is, the continuing resolution increases Congress members' pay by 3.8%, according to a Congressional Research Service report.  Most rank-and-file Congress members make $174,000 annually, meaning they would receive a $6,600 increase for a total salary of $180,600.   This isn’t because lawmakers are including a specific provision that would raise their pay, however. It’s because they’ve left out a provision that would freeze member pay.   The Ethics Reform Act of 1989 established a formula that relies on changes in private sector wages and salaries to determine automatic annual pay adjustments for Congress members, according to the Congressional Research Service. Under that act, salaries are adjusted annually using the formula unless Congress denies it by statute or it is limited by base pay increases for general schedule federal employees.   Two previous versions of 2025 appropriations bills included language that would have prohibited the salary increases lawmakers are allowed by statute. The July Senate bill, for example, included a provision titled: "Limitation on cost of living adjustments for members." That provision said that "notwithstanding any other provision of law, no adjustment shall be made" during fiscal year 2025 related to "cost of living adjustments for Members of Congress."  The continuing resolution did not include a provision freezing the automatic pay increase, meaning members would have received the 3.8% pay increase afforded to them by existing statute."""

# news_vec = vectorization.transform([news])
# print("Real") if (model.predict(news_vec) == 1) else print("Fake")

"""
curl -X POST -H "Content-Type: application/json" -d "" http://localhost:8000/api/v1/fake-news/predict 
"""