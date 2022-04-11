import os
import shutil

address_list = [*os.walk("my_project")]
for address in address_list:
    if "templates" in address[0]:
        if address[1]:
            print(address)
            address_dir = os.path.join(address[0], address[1][0])
            os.makedirs("my_project\\templates", exist_ok=True)
            shutil.move(address_dir, "my_project\\templates")
            shutil.rmtree(os.path.dirname(address_dir))
