import sys
from services.spawn import MobileTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	templates = Vector()
	attacks = Vector()
	attacks.add('bm_bite_1')
	attacks.add('bm_spit_1')
	attacks.add('bm_damage_poison_1')
	mobileTemplates.setAttacks(attacks)
	templates.add('object/mobile/shared_chuba_hue.iff')
	mobileTemplate.setCreatureName('chuba')
	mobileTemplate.setTemplates(templates)
	mobileTemplate.setLevel(5)
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	core.spawnService.addMobileTemplate('chuba', mobileTemplate)
	