df.to_csv("temp.csv")
df = pd.read_csv('temp.csv', index_col=0)

plt.figure(figsize=(5, 5))
sns.set_context('paper', font_scale=1.4)
sns.heatmap(df, annot=True, cmap='Blues', fmt='.3g')
plt.show()


heat_map = sns.heatmap(df, annot=True, cmap='Blues', fmt='.3g')
heat_map.figure.savefig('figure name.png')
