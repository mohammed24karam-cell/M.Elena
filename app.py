<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المرحلة الخامسة - النسخة الكاملة</title>
    <style>
        /* التنسيق العام */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f0f2f5;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        /* الحاوية الرئيسية */
        .container {
            background: white;
            max-width: 600px;
            width: 100%;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            padding: 30px;
            border-top: 8px solid #0984e3;
        }

        /* العناوين */
        h1 { color: #2d3436; text-align: center; font-size: 24px; }
        
        /* البطاقات الصغيرة */
        .card {
            background: #f8f9fa;
            border-right: 5px solid #0984e3;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            transition: 0.3s;
        }

        .card:hover { transform: scale(1.02); background: #eef2f7; }

        /* الأزرار */
        .btn-box { display: flex; gap: 10px; margin-top: 20px; }
        .btn {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s;
        }
        .save-btn { background: #00b894; color: white; }
        .reset-btn { background: #dfe6e9; color: #2d3436; }

        .btn:hover { opacity: 0.8; }
    </style>
</head>
<body>

    <div class="container">
        <h1>✨ مشروع المرحلة الخامسة ✨</h1>
        <p style="text-align: center; color: #636e72;">تم دمج كل المراحل بنجاح</p>

        <div class="card">
            <strong>المرحلة 1-3:</strong> تنسيق المحتوى ومعالجة الصور.
        </div>
        
        <div class="card">
            <strong>المرحلة 4:</strong> البرمجة والمنطق البرمجي.
        </div>

        <div class="card" style="border-right-color: #6c5ce7;">
            <strong>المرحلة 5:</strong> الواجهة الجمالية النهائية.
        </div>

        <div class="btn-box">
            <button class="btn save-btn" onclick="alert('تم الحفظ!')">حفظ العمل</button>
            <button class="btn reset-btn" onclick="location.reload()">تحديث</button>
        </div>
    </div>

</body>
</html>
