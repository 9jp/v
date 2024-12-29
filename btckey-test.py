from bitcoinlib.wallets import Wallet

def is_valid_private_key(private_key):
    try:
        # نحاول إنشاء محفظة جديدة باستخدام المفتاح الخاص المدخل
        Wallet.create('TempWallet', keys=private_key)
        return True
    except Exception:
        # في حال حدوث خطأ، المفتاح الخاص غير صالح
        return False

def check_keys_from_file(input_filename, output_filename):
    valid_keys = []  # قائمة لتخزين المفاتيح الصالحة

    with open(input_filename, 'r') as file:
        keys = file.readlines()
    
    for key in keys:
        key = key.strip()  # إزالة أي مسافات أو أسطر جديدة
        if is_valid_private_key(key):
            print(f"المفتاح الخاص {key} صالح.")
            valid_keys.append(key)  # إضافة المفتاح الصالح إلى القائمة
        else:
            print(f"المفتاح الخاص {key} غير صالح.")
    
    # حفظ المفاتيح الصالحة في ملف جديد
    with open(output_filename, 'w') as valid_file:
        for valid_key in valid_keys:
            valid_file.write(valid_key + '\n')

# استدعاء الدالة مع أسماء الملفات
check_keys_from_file('keys.txt', 'valid_keys.txt')