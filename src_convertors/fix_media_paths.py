import os
import xml.etree.ElementTree as ET

# Get user's home directory and EAF directory path
user_home = os.path.expanduser("~")
base_path = os.path.join(user_home, "tsakorpus", "src_convertors", "corpus", "eaf")

# Loop through all EAF files
for fname in os.listdir(base_path):
    if fname.endswith(".eaf"):
        eaf_path = os.path.join(base_path, fname)
        try:
            tree = ET.parse(eaf_path)
            root = tree.getroot()

            updated = False
            for media_tag in root.iter("MEDIA_DESCRIPTOR"):
                audio_filename = os.path.splitext(fname)[0] + ".wav"

                media_tag.set("MEDIA_URL", audio_filename)
                media_tag.set("RELATIVE_MEDIA_URL", audio_filename)
                media_tag.set("MIME_TYPE", "audio/x-wav")  # ensure it's set too

                updated = True

            if updated:
                tree.write(eaf_path, encoding="UTF-8", xml_declaration=True)
                print(f"✅ Updated: {fname}")
            else:
                print(f"✅ Already correct: {fname}")
        except Exception as e:
            print(f"❌ Error processing {fname}: {e}")
