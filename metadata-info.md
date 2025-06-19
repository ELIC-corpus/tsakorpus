## Metadata Setup

ELAN files and their corresponding audio files (.wav) go through conversion and are organized into .json documents. (src_convertors/eaf2json.py). 

There are two types of metadata-levels: document level and setence level. We can use a combination of speaker-id's (from tier names) and 
interview id's (from file names) to organize metadata keys. Here is an example .json document fresh from the source conversion:

```

"meta": {
        "filename": "corpus/eaf/ckm001-2022-01-16-Trviž_01.eaf"
    },
    "sentences": [
        {
            "lang": 0,
            "meta": {
                "speaker": "TRV01"
            },
            "para_alignment": [
                {
                    "off_end": 9,
                    "off_start": 0,
                    "para_id": 1
                }
            ],
            "src_alignment": [
                {
                    "mtype": "audio",
                    "off_end_sent": 9,
                    "off_end_src": 24.581,
                    "off_start_sent": 0,
                    "off_start_src": 0.0,
                    "src": "ckm001-2022-01-16-Trviž_01-0-0.mp4",
                    "src_id": "0_24581",
                    "true_off_start_src": 0.0
                }

...

```

Then, we can look at the filename: ```ckm001-2022-01-16-Trviž_01.eaf```and find our key in the metadata.csv to populate this field. Then, for each setence, we 
look at the given metadata, which is the speaker id: ```TRV01``` and populate the rest of the fields. So for example, a metadata.csv file that looks like:

| Interview ID | Year | Sex    | Born | Recording Location | Comment | Citation       |
|--------------|------|--------|------|---------------------|---------|----------------|
| ckm001       | 2022 | Female | 1983 | Trviž               | None    | ELIC Citation  |
| ...          | ...  | ...    | ...  | ...                 | ...     | ...            |


Will allow us to populate these fields using the attached script (finalizing fields and organization first). Then, the resulting .json should look like:

```

{
  "meta": {
    "interview_id": "ckm001",
    "year": "2022",
    "recording_location": "Trviž",
    "comment": null,
    "citation": "ELIC Citation"
  },
  "sentences": [
    {
      "lang": 0,
      "meta": {
        "speaker": "TRV01",
        "interview_id": "ckm001",
        "year": "2022",
        "sex": "Female",
        "born": "1983",
        "recording_location": "Trviž",
        "comment": null,
        "citation": "ELIC Citation"
      },
      "para_alignment": [
        {
          "off_end": 9,
          "off_start": 0,
          "para_id": 1
        }
      ],
      "src_alignment": [
        {
          "mtype": "audio",
          "off_end_sent": 9,
          "off_end_src": 24.581,
          "off_start_sent": 0,
          "off_start_src": 0.0,
          "src": "ckm001-2022-01-16-Trviž_01-0-0.mp4",
          "src_id": "0_24581",
          "true_off_start_src": 0.0
        }
      ]
    }
  ]
}

...

```
