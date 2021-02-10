import {month} from './utils'

export const manageText = (text) => {
  if(!text) return ''
  if (text.length > 160) {
	text = text.substring(0, 150)
    return text + '...';
  } else {
    return text
  }
}

export const manageBigText = (text) => {
  if(!text) return ''
  if (text.length > 300) {
    text = text.substring(0, 300)
    return text + '...';
  } else {
    return text
  }
}

export const manageTitle = (name) => {
  if(!name) return ''
  if (name.length > 50) {
	name = name.substring(0, 50)
    return name + '...';
  } else {
    return name
  }
}

export const manageDate = (creation_date) => {
  if(!creation_date) return ''
  creation_date = creation_date.split('-').map(Number)
  return [creation_date[2], String(month[creation_date[1]]).substring(0, 3)]
}