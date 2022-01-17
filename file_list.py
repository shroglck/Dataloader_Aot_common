import os 
import json
def load_frame_for_part(source_path,part):
    path=os.path.join(source_path,part)
    image_data=os.path.join(path,"Images")
    annotation_data=os.path.join(path,"ImageSets")
    annotation_data=os.path.join(annotation_data,"groundtruth.json")
    annotations=open(annotation_data)
    annotation=json.load(annotations)
    print(annotation['metadata'])
    ans=[]
    for ids in annotation['samples'].keys():
        for frames in annotation['samples'][ids]['entities']:
            if frames.get('bb',None):
                flight_path=os.path.join(image_data,ids)
                frame_path=os.path.join(flight_path,frames['img_name'])
                sample={}
                sample["file_path"]=frame_path
                sample["bb"]=frames['bb']
                sample["class"]=frames["id"]
                ans.append(sample)
    return ans