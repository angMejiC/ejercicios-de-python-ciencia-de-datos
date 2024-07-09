from  matplotlib import pyplot as plt


age_x=[25,26,27,28,29,30,31,32,33,34,35]


devx_y=[48496,52000,56752,59320,63200,
       66000,72316,74928,77317,78748,83752]

plt.plot(age_x,devx_y, label='Python')


js_dev_y=[37810,43515,46823,49293,53437,
          56373,62375,66674,68745,68746,74583]
plt.plot(age_x,js_dev_y,linestyle='--', label='JavaScrip')

dev_y=[38496,42000,46752,49320,53200,
       56000,62316,64928,67317,68748,73752]

plt.plot(age_x,dev_y,  label='all devs')

plt.xlabel("ages")
plt.ylabel('Median salary (USD) by Age')
plt.title('Median Salary')

plt.legend()

plt.savefig('plot.png')
plt.tight_layout()

plt.show()