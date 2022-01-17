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
        seen_frame=[]
        for frames in annotation['samples'][ids]['entities']:
            frame_name=frames["img_name"]
            if frame_name not in seen_frame:
                seen_frame.append(frame_name)
                if frames.get('bb',None):
                    flight_path=os.path.join(image_data,ids)
                    frame_path=os.path.join(flight_path,frames['img_name'])
                    sample={}
                    sample["img_name"]=frame_name
                    sample["file_path"]=frame_path
                    sample["bb"]=[frames['bb']]
                    sample["class"]=[frames["id"]]
                    ans.append(sample)
            elif frame_name in seen_frame:
                for sample in ans:
                    if sample["img_name"]==frame_name:
                        sample["bb"].append(frames["bb"])
                        sample["class"].append(frames["id"])
                
    return ans