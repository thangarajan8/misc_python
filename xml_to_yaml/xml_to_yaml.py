import xmlplain

# Read to plain object
with open("sample.xml") as inf:
  root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

# Output plain YAML
with open("sample.yml", "w") as outf:
  xmlplain.obj_to_yaml(root, outf)