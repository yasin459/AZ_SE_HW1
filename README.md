# AZ_SE_HW1
***یاسین موسوی 98110351***

***متین مرادی 98104488***

این ریپو برای تمرین اول درس آزمایشگاه مهندسی نرم افزار است که هدف آن آشنایی با ابزار Git و Github است. برنامه ما به این صورت کار میکند که ابتدا یک فایل متنی داریم که هر کدام از افراد تیم، شماره دانشجویی خود را در آن اضافه میکند. سپس یک برنامه به زبان پایتون نوشته میشود که از فایل متنی مذکور بخواند و بررسی کند که شماره دانشجویی‌ها یکسان هستند یا متفاوت. نهایتا نتیجه را چاپ میکند. 

### راه اندازی
 در این بخش ابتدا با کمک ستور  git init  پروژه گیت را ساختیم. سپس یک فایل note  با مقدار  starter notepad  ساختیم. این فایل را به کمک  git add --all  به استیج شده ها اضافه کردیم و سپس با  git commit -m "some message" آن را کامیت کردیم.

حال در گیتهاب هم یک پروژه ساختیم و و ادرس  url آن را به عنوان remote origin  در گیت محلی خودمان ست کردیم. با اینکار میتوانیم به این ریموت پوش کنیم. با دستور  git push origin master میتوانیم داده ها را به سرور منقل کنیم.

###چند کامیت ابتدایی
در ابتدا چند کامیت بی منظور میزنیم و آنها را به سرور پوش میکنیم. 
### ساخت برنچ
برای ساخت برنچ کافیست تا از دستور  git branch branch_name استفاده کنیم. با کمک همین دستور یک برنچ  names_branch میسازیم که مسعولیت آن اضافه کردن اسامی به فایل note است. سپس به کمک  git checkout names_branch به آن منتقل میشویم.
پس از اعمال تغییرات و کامیت کردن، باید به سرور ارسال کنیم. ولی چون یک شاخه جدید است نیاز داریم تا با دستور  git push -u origin branch_names آن را به ریموت بفرستیم. پس از این هم به حالت عادی به همین شاخه پوش میکنیم. 

به همین ترتیب یک برنج دیگر هم ایجاد میکنیم به نام IDchecker برای کار بر روی برنامه‌ی پایتون مورد نظر. مراحل را مانند بالا طی میکنیم.

### محافظت از شاخه master

برای اینکار در گوگل سرچ کردم و از setting  و سپس  branches بخشی دارد که میتوانیم شاخه ای که میخواهیم محافظت شود را انتخاب کنیم. با انتخاب آن دیگر فقط با  pull request میتوان به آن کد اضافه کرد. حال اگر تغییری در شاخه names_branches و در فایل  note  ایجاد کنیم و پوش کنیم، یک pull request برایمان در گیتهب نمایش داده میشود که با ساختن آن باید منتظر تایید  admin ها باشیم. اگر ادیمن ها تایید کنند کد ما به شاخه اصلی اضافه میشود.

### اضافه کردن gitignore
برای اینکار صرفا یک فایل با همین نام میسازیم و درون آن عبارت *.key را میگذاریم که یعنی فای های با پسوند .key را به سرور نفرست. فایل gitignore باید به سرور فرستاده شود.

### کانفلیکت خوردن 
1. سنناریوی اول این است در names_branches شماره دانشجویی خود را 98110351 زدم و پوش کردم و پول ریکوعست آن را هم اگسپت کردم. سپس بدون پول کردن در  master، اقدام به اضافه کردن شماره دانشجویی خود اینبار با  98110352 کردم که با قبلی تفاوت دارد. این را هم کامیت کرده و سعی کردم پوش کنم و خب نشد. 

![image](https://github.com/yasin459/AZ_SE_HW1/assets/60640286/d1a402a4-7cb4-4ed4-9a5f-84deffca75a5)

بنابراین ابتدا پول کردم و دوباره سعی کردم که پوش کنم:

![image](https://github.com/yasin459/AZ_SE_HW1/assets/60640286/a23a5b06-08c8-453b-ba37-3ad61e65ac64)

باز هم نشد، حال فایل را باز میکنیم و نشانه های git  را برای اضافه و کم کردن مشاهده میکنیم و تغییرات لازم را اعمال میکنیم:

![image](https://github.com/yasin459/AZ_SE_HW1/assets/60640286/994b5b6a-3093-49c1-b8d9-32fc91991010)

اینبار پوش میکنیم و به درستی عملیات انجام میشود:
![image](https://github.com/yasin459/AZ_SE_HW1/assets/60640286/1d99d9d1-27f2-4f86-85e6-dad7d906fcfa)


2. سناریوی دوم این بود که در فایل note.txt در برنچ names_branch عبارت moradi به شکل morady نوشته شد. کامیت و پوش شد. در وهله‌ی بعدی، روی برنچ IDchecker آمدیم و سپس در همان فایل note.txt عبارت moradi به شکل moradii نوشته شد و کامیت شد. حال در قدم بعدی، git merge names_branch را میزنیم تا تغییراتی که در برنچ names_branch دادیم، در هنگام ادغام با برنچ فعلی، به کانفلیکت بخورد:
![image](https://github.com/yasin459/AZ_SE_HW1/assets/62210384/0d4fd9b8-9276-4c49-aeb3-70090dd67af5)

درنهایت کافلیکت را برطرف میکنیم و عملیات ادغام را انجام میدهیم که به صورت موفقیت آمیزی انجام میگیرد:
![image](https://github.com/yasin459/AZ_SE_HW1/assets/62210384/c9cb1908-0d27-4af9-b8e5-e7d1b1211bc4)

## پرسش‌ها

1. پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟
   
    انی پوشه حاوی تمامی اطلاعت ذخیره شده توسط گیت برای پروژه مربوطه است. به طوریکه اطلاعات تمامی تغییرات، کامیت ها، شاخه ها، تنظیمات پروژه و ... در آن نگهداری میشود. برای ساخت این پوشه باید از  git init  استفاده کنیم.

   
2. منظور از atomic بودن در atomic commit و atomic pull-request چیست؟

طبق سرچ و مطالعه‌ای که کردم، میتوان از دو جنبه به atomic بودن نگاه کرد. یکی اینکه وقتی میگوییم commitها یا pull-requestها به شکل atomic اعمال میشوند، یعنی همه یا هیچ. یعنی کل آن تغییرات به شکل یک واحد یکتا درنظر گرفته میشوند فلذا یا همه‌ی آن تغییرات اعمال میشوند و یا در صورت ایجاد مشکل، هیچکدام تاثیر داده نمیشوند. به این شکل سازگاری تضمین خواهد شد. معنای دومی که از atomic بودن برداشت میشود و به شکل توصیه به کار میرود، این است که کامیت‌ها باید به شکل واحدهای کوچک زده شوند و هرکدام یک task مشخص را جلو برده باشند. این کار باعث میشود فرایند undo , revert یک تغییر خاص، review کردن و ... آسان‌تر شود و به شکل کلی تغییرات، به شکل شفاف‌تری قابل رصد باشند. 


4. تفاوت دستورهای fetch و pull و merge را بیان کنید.
   
   دستورهای fetch، pull و merge هر سه برای کار با تغییراتی که در یک مخزن از روی یک مخزن دیگر اعمال شده‌اند، استفاده می‌شوند. با این حال، هر کدام از این دستورها اهداف متفاوتی دارند و در شرایط مختلفی مورد استفاده قرار می‌گیرند. تفاوت اصلی این سه دستور در مراحلی است که در آن‌ها تغییرات دیگری از روی مخزن اصلی به مخزن محلی شما منتقل می‌شوند.

دستور fetch: با استفاده از این دستور، تغییراتی که از روی مخزن اصلی انجام شده‌اند را دریافت و به مخزن محلی خود منتقل می‌کنید، اما هیچ تلاشی برای ادغام آن‌ها با تغییرات محلی شما انجام نمی‌دهد. به عبارت دیگر، دستور fetch فقط تغییرات را دریافت می‌کند، اما تغییرات را در مخزن محلی شما اعمال نمی‌کند.

دستور pull: این دستور با استفاده از دستور fetch تغییراتی که از روی مخزن اصلی انجام شده‌اند را دریافت و به مخزن محلی شما منتقل می‌کند. سپس به صورت خودکار تلاش می‌کند برای ادغام تغییرات محلی و تغییراتی که از مخزن اصلی دریافت کرده، انجام شود. به عبارت دیگر، دستور pull تغییرات را دریافت کرده و همچنین تلاش می‌کند برای ادغام آن‌ها با تغییرات محلی شما.

دستور merge: این دستور به شما اجازه می‌دهد تا دو شاخه (برنچ) را با یکدیگر ادغام کنید. به عبارت دیگر، با استفاده از دستور merge، تغییرات موجود در یک شاخه را با تغییرات موجود در شاخه دیگری که می‌خواهید با آن آن را ادغام کنید، ترکیب می‌کنید. این دستور معمولاً بعد از دستور fetch و pull برای ادغام تغییرات محلی و تغییراتی که از مخزن اصلی دریافت شده‌اند، استفاده می‌شود.


4. تفاوت چهار دستور reset و revert و rebase و restore را بیان کنید.

* دستور restore: با استفاده از این دستور میتوان تغییرات کامیت نشده را دور انداخت و برگشت به آخرین حالت کامیت شده. این حالت وقتی میخواهیم به حالات قبلی برگردیم درعین اینکه تاریخچه‌ی کامیت‌ها عوض نشود، قابل استفاده است.
* دستور reset: این دستور برای ریست کردن working directory به یک کامیت مشخص استفاده میشود یعنی HEAD و کامیت کنونی را برمیگرداند به یک استیت دلخواه قبلی و تاریخچه‌ی کامیت‌ها و branch history را هم تغییر میدهد.
* دستور revert: این دستور مشابه دستور قبلی است ولی تفاوت مهمی که دارد این است که برای هر عملیات revert، یک کامیت جدید ایجاد میکند و به این شکل یک رااه امن‌تر برای undo کردن کامیت‌ها می‌باشد.
* دستور rebase: با این دستور، میتوان base یک دنباله از کامیت‌ها را تغییر داد. به عبارت ساده‌تر، وقتی base یک برنچ را از کامیت A به کامیت B تغییر میدهیم، انگار درشکل جدید، برنچ را از B ایجاد کرده‌ایم نه از A. شکل زیر، این فرایند را بهتر نشان میدهد:
![image](https://github.com/yasin459/AZ_SE_HW1/assets/62210384/41e407db-f254-4e6a-8dfb-40dbf1da46b5)
این کار در قالب برنچ feature بیشتر مورد استفاده قرار میگیرد و به طور کلی برای داشتن یک commit history تمیز و سامان‌یافته، قابل استفاده است.

   
5. منظور از stage چیست؟ دستور stash چه کاری را انجام می‌دهد؟

استیج کردن به عنوان عملی بین ایجاد تغییرات در دایرکتوری موجودمان و تغییرات کامیت شده شناخته میشود. وقتی تغییراتی در فایلها ایجاد میکنیم، گیت آنها را ابتدائاً در حالت "unstaged" درنظر میگیرد. برای همین است که وقتی میخواهیم کامیت کنیم، ابتدا نیاز است که دستور git add folanfile.py را بزنیم تا مشخص شود قصد داریم چه تغییراتی در کامیت لحاظ شوند و کدام‌ها لحاظ نشوند.
دستور stash یک snapshot از تغییراتی که تا اینجا روی فایلها داده‌ایم ولی هنوز کامیت نکرده‌ایم، در یک فضای پنهان به نام "stash" نگهداری می‌کند. آنگاه میتوانیم با خیال راحت مثلا بین برنچ‌ها جابجا شویم و هرموقع که به آن برنچ اول برگشتیم، با زدن دستور git stash apply تغییرات stash شده را دوباره برمیگرداند.


7. مفهوم snapshot به چه معناست؟
   
مفهوم snapshot، به معنای وضعیت کل ریپازیتوری در یک زمان خاص است یعنی state همه‌ی محتواها و اطلاعات مربوط به فایل‌های ترک شده‌ی پروژه. وقتی کامیت میزنیم، گیت درواقع یک snapshot جدید میسازد و نگهداری میکند به همین دلیل است که میگویند: "commits are snapshots, not diffs". استفاده از اسنپ‌شات فوایدی مانند سرعت بیشتر و integrity داده را برای ما به ارمغان دارد.





