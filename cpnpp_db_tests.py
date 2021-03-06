#!/usr/bin/python
# coding=utf-8

import datetime
import unittest

from app import app
from models import (db, Accession, Address, AmountUsed, Availability, Contact, Entity, GeoLocation, Release, SeedUse,
                    Shipment, Species, Testing, Visit, Zone)


def create_app():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    return app


class AccessionTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        self.plant1 = Species(symbol='ABAB', name_full='Abutilon abutiloides', common='shrubby Indian mallow',
                              family='Malvaceae', genus='Abutilon', species='abutiloides', var_ssp1=None, var_ssp2=None,
                              plant_type=None, plant_duration=None, priority_species=0, gsg_val=0,
                              poll_val=0, research_val=0)
        self.synonym1 = Species(symbol='ABAM5', name_full='Abutilon americanum', common='shrubby Indian mallow',
                                family='Malvaceae', genus='Abutilon', species='americanum', var_ssp1=None,
                                var_ssp2=None, plant_type=None, plant_duration=None, priority_species=0, gsg_val=0,
                                poll_val=0, research_val=0)
        self.synonym2 = Species(symbol='ABJA', name_full='Abutilon jacquinii', common='shrubby Indian mallow',
                                family='Malvaceae', genus='Abutilon', species='jacquinii', var_ssp1=None, var_ssp2=None,
                                plant_type=None, plant_duration=None, priority_species=0, gsg_val=0,
                                poll_val=0, research_val=0)
        self.synonym3 = Species(symbol='ABLA', name_full='Abutilon lignosum', common='shrubby Indian mallow',
                                family='Malvaceae', genus='Abutilon', species='lignosum', var_ssp1=None, var_ssp2=None,
                                plant_type=None, plant_duration=None, priority_species=0, gsg_val=0,
                                poll_val=0, research_val=0)
        self.address1 = Address(address_one='P.O. Box 1029', address_two='1117 N. Main Street', state='UT',
                                city='Monticello', zipcode=84535)
        self.address2 = Address(address_one='271 W Bitterbrush Lane (aka Prison Road)', address_two='Green Building',
                                city='Draper', state='UT', zipcode=840209599)
        self.contact1 = Contact(first_name='Mark', last_name='Grover', email='mgrover@fourcornersschool.org',
                                telephone=4355872156, tel_ext=1024, title='Conservation Coordinator', agency=None,
                                address=self.address1)
        self.contact2 = Contact(first_name='Tom', last_name='Glass', email='tom@highmtnnursery.com',
                                telephone=2084216904, tel_ext=None, title='Owner', address=self.address2)
        self.entity1 = Entity(name='Four Corners School of Outdoor Education', address=self.address1,
                              contacts=[self.contact1], request_costs=1, cost=35.00,
                              entity_email='info@fourcornersschool.org', entity_phone=4355872156, entity_phone_ext=1010)
        self.entity2 = Entity(name='High Mountain Nursery', address=self.address2, contacts=[self.contact2],
                              request_costs=0, cost=None, entity_email='info@highmountainnursery.com',
                              entity_phone='8010001111', entity_phone_ext=10)
        self.zone1 = Zone(ptz='10 - 15 Deg. F./6 - 12', us_l4_code='20c',
                          us_l4_name='Semiarid Benchlands and Canyonlands', us_l3_code='20',
                          us_l3_name='Colorado Plateaus', achy_sz_gridcode=11, achy_sz_zone='L1L2H3',
                          aslo3_sz_gridcode=3, aslo3_sz_zone='H1L2H3', bogr2_sz_gridecode=1, bogr2_sz_zone='M1L2H3',
                          cllu2_sz_gridcode=2, cllu2_sz_zone='L1H2H3', elel5_sz_gridcode=4, elel5_sz_zone='M1H2H3',
                          maca2_sz_gridcode=5, maca2_sz_zone='H1H2H3', plja_sz_gridcode=6, plja_sz_zone='H2H3H3',
                          sppa2_sz_gridcode=7, sppa2_sz_zone='H1H2H3', cp_buff=1, cp_strict=1, avail_buff=1,
                          avail_strict=0, usgs_zone=0)
        self.zone2 = Zone(ptz='10 - 15 Deg. F./3 - 6', us_l4_code='79c',
                          us_l4_name='Madrean Pine-Oak and Mixed Conifer Forests', us_l3_code='79',
                          us_l3_name='Madrean Archipelago', achy_sz_gridcode=0, achy_sz_zone='None',
                          aslo3_sz_gridcode=3, aslo3_sz_zone='H1L2H3', bogr2_sz_gridecode=1, bogr2_sz_zone='M1L2H3',
                          cllu2_sz_gridcode=2, cllu2_sz_zone='L1H2H3', elel5_sz_gridcode=4, elel5_sz_zone='M1H2H3',
                          maca2_sz_gridcode=5, maca2_sz_zone='H1H2H3', plja_sz_gridcode=6, plja_sz_zone='H2H3H3',
                          sppa2_sz_gridcode=7, sppa2_sz_zone='H1H2H3', cp_buff=0, cp_strict=0, avail_buff=None,
                          avail_strict=None, usgs_zone=None)
        self.geo_location1 = GeoLocation(land_owner='BLM', geology='Quaternary alluvial terrace deposits',
                                         soil_type='brown-tan sand', phytoregion='25E',
                                         phytoregion_full='Western High Plains (Omernik)',
                                         locality='Grand Staircase Escalante National Monument',
                                         geog_area='Big Cottonwood Canyon',
                                         directions=('Head NE on HWY 62/180 for 30 miles and turn left on '
                                                     'county road 243. Continue on 243 for 8.3 miles then turn left '
                                                     'onto county toad 126A. Continue on 126A for 12 miles then turn '
                                                     'right. Continue for approximately 1.1 miles to reach collection '
                                                     'site.'), degrees_n=38, minutes_n=20, seconds_n=16.32,
                                         degrees_w=107, minutes_w=53, seconds_w=59.64, latitude_decimal=38.33786,
                                         longitude_decimal=-107.8999, georef_source='GPS', gps_datum='NAD83',
                                         altitude=7100, altitude_unit='ft', altitude_in_m=2164,
                                         fo_name='UNCOMPAHGRE FIELD OFFICE', district_name='SOUTHWEST DISTRICT OFFICE',
                                         state='CO', county='Montrose', zone=self.zone1)
        self.geo_location2 = GeoLocation(land_owner='USFS', geology='Quaternary and tertiary upper Santa Fe group',
                                         soil_type='Loamy fine sand, 7.5YR 5/6, strong brown', phytoregion='24E',
                                         phytoregion_full='Chihuahuan Deserts (Omernik)', locality='Red Sands OHV area',
                                         geog_area='None',
                                         directions=('Going south on highway 54 from Alamagordo, drive 18 miles and '
                                                     'make a right on dirt road. Proceed ca. 0.25 miles, make a left'
                                                     'on 2-track road over sand dunes. Drive ca. 0.5 miles.'),
                                         degrees_n=32, minutes_n=36, seconds_n=28.4, degrees_w=106, minutes_w=00,
                                         seconds_w=46.4, latitude_decimal=32.60788, longitude_decimal=-106.01288,
                                         georef_source='GPS', gps_datum='NAD83', altitude=3960, altitude_unit='ft',
                                         altitude_in_m=1207.007961, fo_name='LAS CRUCES DISTRICT OFFICE',
                                         district_name='NEW MEXICO STATE OFFICE', state='NM', county='Otero',
                                         zone=self.zone1)
        self.visit1 = Visit(date=datetime.date.today(),
                            associated_taxa_full=('Quercus gambelii, Ericameria nauseosa ssp. consimilis var. nitida, '
                                                  'Artemisia tridentata ssp. wyomingensis, Lepidium sp., Rosa woodsii, '
                                                  'Heterotheca villosa var. villosa, Carex geyeri, Koeleria macrantha'),
                            mod='grazed, trampled', mod2='recreation', slope='5-25 degrees',
                            aspect='varied', habitat='Mountain Brush; meadow along road', population_size=200,
                            accession=None, geo_location=self.geo_location1, species=self.plant1)
        self.visit2 = Visit(date=datetime.date.today(),
                            associated_taxa_full=('Artemisia filigolia, Amsonia tomentosa var. stenophylla,'
                                                  'Palafoxia sphacelata, Sporobolus giganteus, Prosopsis glandulosa,'
                                                  'Baileya multiradiata, Atriplex canescens'),
                            mod='Grazed', mod2='Livestock grazing, recreation', slope='5-25 degrees',
                            aspect='varied', habitat='Mountain Brush; meadow along road', population_size=200,
                            accession=None, geo_location=self.geo_location2, species=self.synonym1)
        self.accession1 = Accession(data_source='UP', plant_habit='Forb/herb',
                                    coll_date=datetime.date(year=2004, month=8, day=24), acc_num='UP-76', acc_num1='UP',
                                    acc_num2='76', acc_num3=None, collected_with='GVR, CH, SP',
                                    collection_misc=('Hand-pick ripe seeds, all stages still on plants. This Aster '
                                                     'glaucodes is in a nice loamy field (not rocky cliff like other '
                                                     'Aster glaucodes)'),
                                    seed_source='P', description='Height: 0.15-0.45 m',
                                    notes=('Official SOS collection number is NM930N-69: details submitted to SOS '
                                           'National Office by Farmington BLM Botanist. Germination and competition '
                                           'trials for early seral species (Chicago Botanic Garden).  Photos of '
                                           'habitat, plant and seed'), increase=0, species=self.plant1,
                                    geo_location=self.geo_location1, occupancy=300)
        self.accession2 = Accession(data_source='BGB', plant_habit='Forb/herb',
                                    coll_date=datetime.date(year=2010, month=7, day=28), acc_num='WY040-42',
                                    acc_num1='WY040', acc_num2='42', acc_num3=None,
                                    collected_with='Giles, R., Lerer, A., Gray, T., Fouts, D., Kobelt, L.',
                                    collection_misc='2000 plants sampled', seed_source='P',
                                    description='Height: 0.15-0.45 m',
                                    notes=('Official SOS collection number is NM930N-69: details submitted to SOS '
                                           'National Office by Farmington BLM Botanist. Germination and competition '
                                           'trials for early seral species (Chicago Botanic Garden).  Photos of '
                                           'habitat, plant and seed'), increase=0, species=self.synonym1,
                                    geo_location=self.geo_location2, occupancy=300)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.plant = None
        self.synonym1 = None
        self.synonym2 = None
        self.synonym3 = None
        self.address1 = None
        self.address2 = None
        self.contact1 = None
        self.contact2 = None
        self.entity1 = None
        self.entity2 = None
        self.visit1 = None
        self.visit2 = None
        self.zone1 = None
        self.zone2 = None
        self.location1 = None
        self.location2 = None
        self.accession1 = None
        self.accession2 = None

    def test_species_synonym_relationship(self):
        self.plant1.add_synonym(self.synonym1)
        self.plant1.add_synonym(self.synonym2)
        self.plant1.add_synonym(self.synonym3)
        db.session.add(self.synonym1)
        db.session.add(self.synonym2)
        db.session.add(self.synonym3)
        db.session.add(self.plant1)
        db.session.commit()
        self.assertEqual(len(self.plant1.synonyms), 3)
        self.assertEqual(self.synonym1.usda_name, self.plant1)
        self.assertEqual(self.synonym2.usda_name, self.plant1)
        self.assertEqual(self.synonym3.usda_name, self.plant1)

    def test_single_shipment_accession_relationship(self):
        db.session.add(self.entity1)
        db.session.add(self.entity2)
        db.session.add(self.plant1)
        db.session.add(self.geo_location1)
        db.session.add(self.zone1)
        db.session.add(self.visit1)
        db.session.add(self.accession1)
        amount = AmountUsed(amount_gr=3.782, species=self.plant1, accession=self.accession1)
        db.session.add(amount)
        shipment = Shipment(order_date=datetime.datetime.today(), ship_date=datetime.datetime.now(),
                            tracking_num='40012345678', shipper='FedEx', origin_entity=self.entity1,
                            destination_entity=self.entity2, amounts_sent=[amount])
        db.session.add(shipment)
        db.session.commit()
        accessions = shipment.get_accessions()
        self.assertIn(self.accession1, accessions)

    def test_multiple_shipment_accession_relationship(self):
        db.session.add(self.entity1)
        db.session.add(self.entity2)
        db.session.add(self.plant1)
        db.session.add(self.synonym1)
        db.session.add(self.geo_location1)
        db.session.add(self.zone1)
        db.session.add(self.visit1)
        db.session.add(self.accession1)
        amount = AmountUsed(amount_gr=3.782, species=self.plant1, accession=self.accession1)
        amount2 = AmountUsed(amount_gr=0.9923, species=self.synonym1, accession=self.accession2)
        db.session.add(amount)
        db.session.add(amount2)
        shipment = Shipment(order_date=datetime.datetime.today(), ship_date=datetime.datetime.now(),
                            tracking_num='40012345678', shipper='FedEx', origin_entity=self.entity1,
                            destination_entity=self.entity2, amounts_sent=[amount, amount2])
        shipment.add_amount(amount2)
        db.session.add(shipment)
        db.session.commit()
        accessions = shipment.get_accessions()
        self.assertIn(self.accession1, accessions)
        self.assertIn(self.accession2, accessions)

    def test_shipment_institute_relationship(self):
        db.session.add(self.entity1)
        db.session.add(self.entity2)
        db.session.add(self.visit1)
        db.session.add(self.zone1)
        db.session.add(self.geo_location1)
        db.session.add(self.plant1)
        db.session.add(self.accession1)
        amount = AmountUsed(amount_gr=3.782, species=self.plant1, accession=self.accession1)
        db.session.add(amount)
        shipment = Shipment(order_date=datetime.datetime.today(), ship_date=datetime.datetime.now(),
                            tracking_num='40012345678', shipper='FedEx', origin_entity=self.entity1,
                            destination_entity=self.entity2, amounts_sent=[amount])
        db.session.add(shipment)
        db.session.commit()
        self.assertEqual(shipment.origin_entity, self.entity1)
        self.assertEqual(shipment.destination_entity, self.entity2)

    def test_accession_location_relationship(self):
        db.session.add(self.plant1)
        db.session.add(self.visit1)
        db.session.add(self.zone1)
        db.session.add(self.geo_location1)
        db.session.add(self.accession1)
        db.session.commit()
        self.assertEqual(self.accession1.geo_location, self.geo_location1)
        self.assertEqual(self.geo_location1.accession, self.accession1)

    def test_accession_species_relationship(self):
        db.session.add(self.plant1)
        db.session.add(self.visit1)
        db.session.add(self.zone1)
        db.session.add(self.geo_location1)
        db.session.add(self.accession1)
        db.session.commit()
        self.assertIn(self.accession1, self.plant1.accessions.all())
        self.assertEqual(self.accession1.species, self.plant1)

    def test_accession_multiple_species(self):
        accession3 = Accession(data_source='UP', plant_habit='Forb/herb',
                               coll_date=datetime.date(year=2004, month=8, day=24), acc_num='UP-79', acc_num1='UP',
                               acc_num2='76', acc_num3=None, collected_with='GVR, CH, SP',
                               collection_misc=('Hand-pick ripe seeds, all stages still on plants. This Aster '
                                                'glaucodes is in a nice loamy field (not rocky cliff like other '
                                                'Aster glaucodes)'), seed_source='P', description='Height: 0.15-0.45 m',
                               notes=('Official SOS collection number is NM930N-69: details submitted to SOS '
                                      'National Office by Farmington BLM Botanist. Germination and competition '
                                      'trials for early seral species (Chicago Botanic Garden).  Photos of '
                                      'habitat, plant and seed'), increase=0, species=self.plant1,
                               geo_location=self.geo_location1, occupancy=300)
        db.session.add(self.plant1)
        db.session.add(self.accession1)
        db.session.add(accession3)
        db.session.commit()
        acc1_species = self.accession1.species
        acc3_species = accession3.species
        self.assertEqual(acc1_species, acc3_species)
        self.assertIn(self.accession1, acc1_species.accessions.all())
        self.assertIn(self.accession1, acc3_species.accessions.all())
        self.assertIn(accession3, acc1_species.accessions.all())
        self.assertIn(accession3, acc3_species.accessions.all())

    def test_testing_accession_relationship(self):
        db.session.add(self.plant1)
        db.session.add(self.visit1)
        db.session.add(self.zone1)
        db.session.add(self.geo_location1)
        db.session.add(self.accession1)
        db.session.add(self.entity1)
        test = Testing(amt_rcvd_lbs=0.7829348, clean_wt_lbs=0.523494, est_seed_lb=351627,
                       est_pls_lb=297054.4896, est_pls_collected=5346.980813, test_type='XPC',
                       test_date=datetime.date(2003, 3, 12), purity=98, tz=60, fill=90, accession=self.accession1,
                       entity=self.entity1)
        db.session.add(test)
        db.session.commit()
        self.assertEqual(self.accession1, test.accession)
        self.assertIn(test, self.accession1.tests)

    def test_availability_accession_relationship(self):
        db.session.add(self.plant1)
        db.session.add(self.visit1)
        db.session.add(self.zone1)
        db.session.add(self.geo_location1)
        db.session.add(self.accession1)
        avail = Availability(grin_avail=1.47, bend_avail=17.690088, cbg_avail=0, meeker_avail=0,
                             misc_avail=0, ephraim_avail=0, nau_avail=0.512592, accession=self.accession1,
                             misc_avail_ent=None)
        db.session.add(avail)
        db.session.commit()
        self.assertTrue(avail.avail_any)
        self.assertEqual(avail.gr_avail, (1.47 + 17.690088 + 0.512592))
        self.assertEqual(avail.lb_avail, ((1.47 + 17.690088 + 0.512592) * 0.00220462))
        self.assertEqual(avail.sum_gr_no_grin, 17.690088 + 0.512592)
        self.assertTrue(avail.avail_no_grin, True)
        self.assertEqual(avail.sum_lb_no_grin, ((17.690088 + 0.512592) * 0.00220462))
        self.assertEqual(self.accession1, avail.accession)
        self.assertEqual(avail, self.accession1.availability)

    def test_availability_institution_relationship(self):
        db.session.add(self.plant1)
        db.session.add(self.visit1)
        db.session.add(self.zone1)
        db.session.add(self.geo_location1)
        db.session.add(self.accession1)
        db.session.add(self.entity1)
        avail = Availability(grin_avail=1.47, bend_avail=17.690088, cbg_avail=0, meeker_avail=0,
                             misc_avail=0, ephraim_avail=0, nau_avail=0.512592, accession=self.accession1,
                             misc_avail_ent=self.entity1)
        db.session.add(avail)
        db.session.commit()
        self.assertEqual(self.entity1, avail.misc_avail_ent)
        self.assertIn(avail, self.entity1.availability)

    def test_use_creation(self):
        db.session.add(self.plant1)
        db.session.add(self.visit1)
        db.session.add(self.zone1)
        db.session.add(self.geo_location1)
        db.session.add(self.accession1)
        amount = AmountUsed(amount_gr=3.782, species=self.plant1, accession=self.accession1)
        use = SeedUse(project_name='Andrea\'s functional trait study',
                      purpose=("We’re planning to set up a field study that is a combination common garden and "
                               "diversity trial (are there differences in functional traits between populations AND do "
                               "we get a boost in productivity/seed production/etc when plants from different "
                               "populations (of the same species) are grown together."), abstract=None,
                      date_start=datetime.date(2017, 9, 1), date_end=None,
                      start_notes=("I'm also interested in tackling the question Scott Jensen raised of incorporating "
                                   "Colorado Plateau accessions in their Great Basin production beds to produce diverse"
                                   " seed that can be used throughout a provisional seed zone. I worked with the "
                                   "species they're thinking of trying this with (Penstemon pachyphyllus) for my "
                                   "dissertation, and found significant outbreeding depression during the first "
                                   "generation when I artificially crossed populations between the Great Basin and "
                                   "Colorado Plateau ecoregions. I of course haven't published this stuff, but have "
                                   "talked with Scott about it. I’ve published everything else I did on the species "
                                   "(molecular and common garden research, but not the outbreeding stuff – I’m "
                                   "attaching very brief summary slides here, and my thesis is also available to "
                                   "download through the GBNPP website if anyone wants the nitty gritty details). The "
                                   "potential for outbreeding depression to have strong and lasting impacts on seed "
                                   "produced is clearly something that needs to be sorted as the GB develops material "
                                   "for species that occur in the CP. Other species that Scott mentioned where I think "
                                   "we can help tackle this question include Heliomeris (but again the ssp issues comes"
                                   " up), Machaeranthera canescens, and Linum lewisii, which is a key reason we’re "
                                   "focusing on them now."), end_notes=None, amounts_used=[amount])
        db.session.add(use)
        self.contact1.seed_uses.append(use)
        self.contact2.seed_uses.append(use)
        self.entity1.seed_uses.append(use)
        self.entity2.seed_uses.append(use)
        self.plant1.uses.append(use)
        self.accession1.projects.append(use)
        db.session.add(self.contact1)
        db.session.add(self.contact2)
        db.session.add(self.entity1)
        db.session.add(self.entity2)
        db.session.commit()
        self.assertIn(use, self.plant1.uses)
        self.assertIn(use, self.accession1.projects)
        self.assertIn(use, self.contact1.seed_uses)
        self.assertIn(use, self.contact2.seed_uses)
        self.assertIn(use, self.entity1.seed_uses)
        self.assertIn(use, self.entity2.seed_uses)
        self.assertEqual(self.plant1, use.species.filter_by(name_full=self.plant1.name_full).first())
        self.assertEqual(self.accession1, use.accessions.filter_by(acc_num=self.accession1.acc_num).first())

    def test_release_creation(self):
        #db.session.add(self.plant1)
        #db.session.add(self.visit1)
        #db.session.add(self.zone1)
        #db.session.add(self.zone2)
        #db.session.add(self.entity1)
        #db.session.add(self.geo_location1)
        #db.session.add(self.accession1)
        rel = Release(loc_desc='Western Colorado', germ_origin='NRCS', name="'Paloma'", year=1974,
                      release_type='cultivar', plant_origin='native',
                      used_for='soil stabilization and range revegetation',
                      select_criteria='establishment, vigor, and forage production in dry land',
                      special_character='superior seed and forage production',
                      adaptation='Western US', prime_pmc='NMPMC', primary_releasing='NMPMC',
                      secondary_releasing='AZAES, COAES, NMAES', cp_adapted=1, cp_sourced=0,
                      source_num='single source', lb_acre_sow=2.4, lb_acre_yield=200,
                      soil_adap='sandy soil', precip_adap='9-10', elev_adap='3000-7500',
                      release_brochure=('https://www.nrcs.usda.gov/Internet/FSE_PLANTMATERIALS/publica'
                                        'tions/nmpmcrb12138.pdf'),
                      comments=('Steve Parr - collected in NW NM - Rio Arriba county - really good '
                                'product'),
                      accession=self.accession1, species=self.accession1.species, entity=self.entity1,
                      priority_zones=[self.zone1], zones=[self.zone1, self.zone2])
        db.session.add(rel)
        db.session.commit()
        self.assertIn(rel, self.plant1.releases)
        self.assertIn(rel, self.accession1.releases)
        self.assertEqual(self.plant1, rel.species)
        self.assertEqual(self.accession1, rel.accession)

if __name__ == '__main__':
    create_app().app_context().push()
    unittest.main()
