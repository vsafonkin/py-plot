from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

user_path = '/home/vsafonkin/'
df = pd.read_csv(user_path + 'stocks.csv')

c = canvas.Canvas(user_path + 'example.pdf', pagesize=A4)
c.setTitle('Example PDF')
c.drawString(100, 750, "Hello, PDF!")

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

fig, axes = plt.subplots(2, 1, figsize=(12, 6))
sns.lineplot(x=[1, 2, 3], y=[4, 5, 6], ax=axes[0])
sns.lineplot(x=[4, 2, 8], y=[5, 3, 2], ax=axes[1])
plt.savefig("page1.png")
plt.clf()

sns.histplot(data)
plt.savefig("page2.png")


c.drawImage("page1.png", 100, 500, width=400, height=300)
c.showPage()
c.drawString(100, 750, "Second page")
c.drawImage("page2.png", 100, 500, width=400, height=300)

c.save()
