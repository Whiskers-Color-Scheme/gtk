import os
import shutil
import zipfile

colloid_accents = ["Yellow", "Teal", "Red", "Purple", "Green", "Orange"]
whiskers_accents = ["Banana", "Blueberry", "Cherry", "Grape", "Kiwi", "Tangerine"]
modes = ["Dark", "Light"]
dpis = ["", "-hdpi", "-xhdpi"]



def main():

    exec_path = os.path.abspath(os.path.join(__file__, os.pardir));
    themes_dir = "/tmp/whiskers-gtk-builder"

    # Remove unused themes
    for accent in colloid_accents:
        for dpi in dpis:
            dir = f"{themes_dir}/Colloid-{accent}-Whiskers{dpi}"

            if os.path.isdir(dir):
                shutil.rmtree(dir)

    for entry in os.listdir(themes_dir):
        if "Colloid" in entry:
            dir = f"{themes_dir}/{entry}"
            new_dir = entry
            new_dir = new_dir.replace("Whiskers-", "")
            new_dir = new_dir.replace("-Whiskers", "")
            new_dir = new_dir.replace("Colloid", "Whiskers")
            new_dir = new_dir.replace("Dark", "Panther")
            new_dir = new_dir.replace("Light", "Tiger")
            new_dir = new_dir.replace("Yellow", "Banana")
            new_dir = new_dir.replace("Teal", "Blueberry")
            new_dir = new_dir.replace("Red", "Cherry")
            new_dir = new_dir.replace("Purple", "Grape")
            new_dir = new_dir.replace("Green", "Kiwi")
            new_dir = new_dir.replace("Orange", "Tangerine")

            new_dir = f"{themes_dir}/{new_dir}"

            if not os.path.isdir(new_dir):
                os.rename(dir, new_dir)


    zips_dir = f"{exec_path}/themes"

    if os.path.isdir(zips_dir):
        shutil.rmtree(zips_dir)

    os.mkdir(zips_dir) 

    for scheme in ["Panther", "Tiger"]:
        for accent in whiskers_accents:        
            print(f"Making Whiskers-{scheme}-{accent}.zip ...")

            base_dir = f"{themes_dir}/Whiskers-{accent}-{scheme}"
            dirs = [base_dir, f"{base_dir}-hdpi", f"{base_dir}-xhdpi"]

            zip_file = zipfile.ZipFile(f"{zips_dir}/Whiskers-{scheme}-{accent}.zip", 'w', zipfile.ZIP_DEFLATED)
            
            for dir in dirs:
                for root, dirs, files in os.walk(dir):
                    for file in files:
                        zip_file.write(os.path.join(root, file), os.path.join(root, file).replace("/tmp/whiskers-gtk-builder/", ""))

            zip_file.close()
        
    print("✅ Themes built successfully")

if __name__ == "__main__":
    main()