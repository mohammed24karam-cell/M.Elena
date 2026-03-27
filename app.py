<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>مشروع المرحلة الخامسة المتكامل | 2026</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    
    <style>
        /* [المرحلة 1 & 2]: الألوان والهوية البصرية */
        :root {
            --primary-blue: #0984e3;      /* أزرق احترافي للمهام */
            --accent-purple: #6c5ce7;    /* بنفسجي للمسات الجمالية */
            --bg-light: #f1f2f6;        /* خلفية مريحة للعين */
            --white: #ffffff;
            --text-dark: #2d3436;
        }

        body {
            font-family: 'Tajawal', 'Cairo', sans-serif;
            background: var(--bg-light);
            margin: 0;
            padding: 30px;
            display: flex;
            justify-content: center;
        }

        /* [المرحلة 3 & 4]: هيكل الحاوية والمنطق التنظيمي */
        .main-wrapper {
            background: var(--white);
            width: 100%;
            max-width: 850px;
            border-radius: 25px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
            border-top: 12px solid var(--primary-blue);
            animation: fadeIn 0.8s ease;
        }

        .header-bg {
            background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
            color: white;
            padding: 40px 20px;
            text-align: center;
        }

        .content-body {
            padding: 40px;
        }

        /* [المرحلة 5]: اللمسات الجمالية وحركات التفاعل */
        .feature-card {
            background: #f9f9f9;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 15px;
            border-right: 6px solid var(--primary-blue);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .feature-card:hover {
            transform: scale(1.03) translateX(-5px);
            background: white;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            border-right-color: var(--accent-purple);
        }

        .step-label {
            font-weight: bold;
            color: var(--primary-blue);
            font-size: 0.8rem;
            text-transform: uppercase;
        }

        .btn-group {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 30px;
        }

        .btn {
            padding: 15px;
            border: none;
            border-radius: 12px;
            font-family: 'Tajawal', sans-serif;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn-main { background: var(--primary-blue); color: white; }
        .btn-outline { background: #dfe6e9; color: var(--text-dark); }

        .btn:hover { opacity: 0.9; transform: translateY(-2px); }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <div class="main-wrapper">
        <div class="header-bg">
            <h1 style="margin: 0; font-size: 2.2rem;">المشروع المدمج النهائي ✨</h1>
            <p style="opacity: 0.9;">تم تجميع كافة المراحل (1-5) في نظام واحد</p>
        </div>

        <div class="content-body">
            <div class="feature-card">
                <div>
                    <span class="step-label">المرحلة 1 & 2</span>
                    <h3 style="margin: 5px 0;">تنسيق WPS والمحتوى التعليمي</h3>
                </div>
                <span>📝</span>
            </div>

            <div class="feature-card">
                <div>
                    <span class="step-label">المرحلة 3</span>
                    <h3 style="margin: 5px 0;">المعالجة الفنية والتصميم البصري</h3>
                </div>
                <span>🎨</span>
            </div>

            <div class="feature-card">
                <div>
                    <span class="step-label">المرحلة 4</span>
                    <h3 style="margin: 5px 0;">برمجة الربط والمنطق الذكي</h3>
                </div>
                <span>💻</span>
            </div>

            <div class="feature-card" style="border-right-color: #00b894;">
                <div>
                    <span class="step-label">المرحلة 5</span>
                    <h3 style="margin: 5px 0;">الواجهة النهائية وتجربة المستخدم</h3>
                </div>
                <span>🚀</span>
            </div>

            <div class="btn-group">
                <button class="btn btn-main" onclick="alert('تم حفظ كل شيء بنجاح!')">حفظ العمل الجديد</button>
                <button class="btn btn-outline" onclick="location.reload()">إعادة تحميل الواجهة</button>
            </div>
        </div>
        
        <footer style="text-align: center; padding: 20px; color: #b2bec3; font-size: 0.8rem;">
            تطوير ذكي | جميع المراحل مدمجة | 2026
        </footer>
    </div>

</body>
</html>
