"""
Author: Chinchien Lin
Email: clin864@auckland.ac.nz
Organisation: ABI clinical translation technology group

primary package: dicomanonymizer: https://pypi.org/project/dicom-anonymizer/
anonymisation for DICOM based on HIPAA standard and with custom rules
"""

import os

import pydicom
import dicomanonymizer as anonymizer


def replace_by_anon_id(dataset, tag):
    element = dataset.get(tag)
    if element is not None:
        element.value = anon_id


def define_custom_rules():
    extra_rules = {}

    tags_to_keep = [
        (0x0010, 0x1010),  # Patient's Age
        (0x0010, 0x1030),  # Patient's Weight
        (0x0010, 0x1020)  # Patient's Size
    ]
    for tag in tags_to_keep:
        extra_rules[tag] = anonymizer.keep
    # for tag in anonymizer.ALL_TAGS:
    #     extra_rules[tag] = anonymizer.keep

    tags_replaced_by_anon_id = [
        (0x0010, 0x0020),  # Patient ID
        (0x0010, 0x0010)  # Patient Name
    ]
    for tag in tags_replaced_by_anon_id:
        extra_rules[tag] = replace_by_anon_id

    return extra_rules


if __name__ == '__main__':
    # set inputs
    input_dir = r""
    output_dir = r""
    filename = "" # optional, if provided, will only anonymise this file in the input_dir
    anon_id = "anon_0001"
    print_result_tags = True

    input_dicom_file = os.path.join(input_dir, filename)
    output_dicom_file = os.path.join(output_dir, filename + "_anonymised")

    extra_rules = define_custom_rules()

    os.makedirs(output_dir, exist_ok=True)
    if filename:
        anonymizer.anonymize(
            input_dicom_file,
            output_dicom_file,
            extra_rules,
            delete_private_tags=False,
        )
        if print_result_tags:
            dcm = pydicom.read_file(output_dicom_file)
            print(dcm)
    else:
        anonymizer.anonymize(
            input_dir,
            output_dir,
            extra_rules,
            delete_private_tags=False,
        )
        if print_result_tags:
            file = os.listdir(output_dir)[0]
            dcm = pydicom.read_file(os.path.join(output_dir, file))
            print(dcm)

