# AZ_SE_HW1
***یاسین موسوی 98110351***

***متین مرادی 985001843***

این ریپو برای تمرین اول درس آزمایشگاه مهندسی نرم افزار است که هدف آن آشنایی با ابزار Git و سپس Github است. برای این اشنایی ما صرفا یک فایل notepad در ویندوز ساختیم و برای آن بخش های مختلف پروژه را اجرا کردیم.

### راه اندازی
 در این بخش ابتدا با کمک ستور  git init  پروژه گیت را ساختیم. سپس یک فایل note  با مقدار  starter notepad  ساختیم. این فایل را به کمک  git add --all  به استیج شده ها اضافه کردیم و سپس با  git commit -m "some message" آن را کامیت کردیم.

حال در گیتهاب هم یک پروژه ساختیم و و ادرس  url آن را به عنوان remote origin  در گیت محلی خودمان ست کردیم. با اینکار میتوانیم به این ریموت پوش کنیم. با دستور  git push origin master میتوانیم داده ها را به سرور منقل کنیم.

###چند کامیت ابتدایی
در ابتدا چند کامیت بی منظور میزنیم و آنها را به سرور پوش میکنیم. 
### ساخت برنچ
برای ساخت برنچ کافیست تا از دستور  git branch branch_name استفاده کنیم. با کمک همین دستور یک برنچ  names_branch میسازیم که مسعولیت آن اضافه کردن اسامی به فایل note است. سپس به کمک  git checkout names_branch به آن منتقل میشویم.
پس از اعمال تغییرات و کامیت کردن، باید به سرور ارسال کنیم. ولی چون یک شاخه جدید است نیاز داریم تا با دستور  git push -u origin branch_names آن را به ریموت بفرستیم. پس از این هم به حالت عادی به همین شاخه پوش میکنیم.