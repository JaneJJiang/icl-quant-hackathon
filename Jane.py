import quandl
import datetime
import pandas as pd

quandl.ApiConfig.api_key = 'ekc-KvBqnKyK6s6CvNoX'

def create_dataset(stream="SMA/FBD",today=datetime.date(2019,9,30), brand="AMZN", Sample=365):
    output=[]
    for d in range(Sample):
        date=today-datetime.timedelta(days=Sample-d)
        try:
            price = quandl.get('EOD/' + brand, start_date=date, end_date=date).Close
            Price = float(price)
            try:
                Change = Price - OldPrice
            except:
                Change = 0
            SocialMedia = quandl.get_table(stream, brand_ticker=brand, date=date)
            NewFans = 0
            Likes = 0
            Comments = 0
            Shares = 0
            Talks = 0

            for i in range(SocialMedia.shape[0]):
                record=SocialMedia.iloc[[i]]
                NewFans += int(record.new_fans)
                Likes += int(record.admin_post_likes)
                Comments += int(record.admin_post_comments)
                Shares += int(record.admin_post_shares)
                Talks += int(record.people_talking_about)
            row = [str(date), NewFans, Likes, Comments, Shares, Talks, Price, Change]
            output.append(row)
            print(row)
            OldPrice=Price
        except:
            pass
            print("no")
    df=pd.DataFrame(output)
    df.to_csv(r'C:/Users/jane1/Documents/Algothon2019/' + brand + str(Sample) + '.csv', header=("Dates", "NewFans", "Likes", "Comments", "Shares" ,"Talks", "Stock Price", "Change"))

create_dataset(brand="AAPL")
