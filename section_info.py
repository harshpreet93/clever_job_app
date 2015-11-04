import requests
import json

''' 
This class represents a section. Notice that it only has the section_id and num_students fields because
those are the only ones that we need. Other fields could be added as we find a need for them. 
'''
class Section:
	section_id = 0
	num_students = 0

#This function prints the section id and number of students in its parameter section.	
def print_section(section):
	print 'Section ID: '+str(section.section_id)+'    '+'Number of students: '+str(section.num_students)

#This function queries the clever api and returns a list of section objects 
def get_all_sections(api_token):
	r = requests.get('https://api.clever.com/v1.1/sections', headers={'Authorization':'Bearer '+api_token})
	if r.status_code != 200: raise RuntimeError('ERROR OCURRED: check your token and/or connection')
	response = json.loads(r.text)['data']
	result = []
	for section in response:
		curr_section = Section()
		curr_section.section_id = section['data']['id']
		curr_section.num_students = len(section['data']['students'])
		result.append(curr_section)
	return result

if __name__ == '__main__':
	all_sections = get_all_sections('DEMO_TOKEN')

	#get the number of sections in the district
	num_sections = len(all_sections)

	#get total number of students in all the sections
	total_num_students_in_all_sections = sum( map(lambda a: a.num_students, all_sections) )
	average_num_students_per_section = total_num_students_in_all_sections / num_sections
	print 'Average number of students per section is: '+ str(average_num_students_per_section)

	#print a detailed report with the numbers of students in all the sections and the section ID's
	print 'Detailed Report: '
	map(print_section, all_sections)