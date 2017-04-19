#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup
from urllib import FancyURLopener
from indices import limpiar
import urllib2

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def datos_tarjeta(banco,tarjeta=None):
    if not tarjeta:
        return (None,None,None)
    tree = None
    link = {}
    path = {}
    if banco == 'Popular':
        tree = ['div','fullbleed-grid row details','class']
        link = {'clasica':['https://www.popularenlinea.com/clasica'],
                'orbit':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/orbit.aspx'],
                'clasica internacional':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/clasica-facturation-en-dolares.aspx'],
                'prestige':['https://www.popularenlinea.com/visaprestige'],
                'gold':['https://www.popularenlinea.com/gold'],
                'gold internacional':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/gold-facturacion-en-dolares.aspx'],
                'platinum':['https://www.popularenlinea.com/platinum'],
                'platinum internacional':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/platinum-dolares.aspx'],
                'black':['https://www.popularenlinea.com/mastercardblack'],
                'black internacional':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/mastercard-black-dolares.aspx'],
                'fcbescola':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/Tarjeta-Credito-FCBEscola.aspx'],
                'jetblue':['https://www.popularenlinea.com/jetblue'],
                'ccn plus':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/mastercard-ccnpPlus.aspx'],
                'mileage plus':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/mastercard-mileage-plus.aspx'],
                'mb signature':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/mb-visa-signature-card.aspx'],
                'ikea family':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/ikea-family.aspx'],
                'seguros universal':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/mc-seguros.aspx'],
                'caminantes por la vida':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/caminantes-por-la-vida.aspx'],
                'almacenes iberia':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/mastercard-almacenes-iberia.aspx'],
                'sirena':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/visa-pola-sirena.aspx'],
                'avanza':['https://www.popularenlinea.com/Personas/Paginas/tarjetas/avanza.aspx']}

        path = {'clasica':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'orbit':['div','col-md-4 col-sm-4 col-xs-12'],
                'clasica internacional':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'prestige':['div','row grid-line-row'],
                'gold':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'gold internacional':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'platinum':['div','col-md-4 col-sm-4 col-xs-12'],
                'platinum internacional':['div','col-md-4 col-sm-4 col-xs-12'],
                'black':['div','col-md-4 col-sm-4 col-xs-12'],
                'black internacional':['div','col-md-4 col-sm-4 col-xs-12'],
                'fcbescola':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'jetblue':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'ccn plus':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'mileage plus':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'mb signature':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'ikea family':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'seguros universal':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'caminantes por la vida':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'almacenes iberia':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'sirena':['div','col-md-3 col-sm-3 col-xs-12 grid-item'],
                'avanza':['div','col-md-3 col-sm-3 col-xs-12 grid-item']}

    if banco == 'LopezDeHaro':
        tree = ['table','tabla-verticalA','class']
        link = {'clasica':['http://www.blh.com.do/Inicio/Productos/Tarjetas-de-cr%C3%A9dito.aspx'],
                'casa de espana':['http://www.blh.com.do/Inicio/Productos/Tarjetas-de-cr%C3%A9dito.aspx'],
                'club hemingway':['http://www.blh.com.do/Inicio/Productos/Tarjetas-de-cr%C3%A9dito.aspx'],
                'club naco':['http://www.blh.com.do/Inicio/Productos/Tarjetas-de-cr%C3%A9dito.aspx'],
                'gold':['http://www.blh.com.do/Inicio/Productos/Tarjetas-de-cr%C3%A9dito.aspx'],
                'golds gym':['http://www.blh.com.do/Inicio/Productos/Tarjetas-de-cr%C3%A9dito.aspx'],
                'platinum':['http://www.blh.com.do/Inicio/Productos/Tarjetas-de-cr%C3%A9dito.aspx']}

        path = {'clasica':['td','tabla-verticalA_celdaAzul'],
                'casa de espana':['td','tabla-verticalA_celdaAzul'],
                'club hemingway':['td','tabla-verticalA_celdaAzul'],
                'club naco':['td','tabla-verticalA_celdaAzul'],
                'gold':['td','tabla-verticalA_celdaAzul'],
                'golds gym':['td','tabla-verticalA_celdaAzul'],
                'platinum':['td','tabla-verticalA_celdaAzul']}
    if banco == 'Progreso':
        tree = ['div','overview_wrap','id']
        link = {'casa de campo':['http://www.americanexpress.com.do/personal/our-cards/TC_platinum_casadecampo.html'],
                'american express':['http://www.americanexpress.com.do/personal/our-cards/TC_personal.html'],
                'american express gold':['https://www.livegold.do/'],
                'suma ccn':['http://www.americanexpress.com.do/personal/our-cards/TC_suma_ccn.html'],
                'gold':['http://www.progreso.com.do/index.php/tarjetas-de-credito-mastercard-gold-internacional'],
                'internacional':['http://www.progreso.com.do/index.php/tarjetas-de-credito-mastercard-internacional'],
                'local':['http://www.progreso.com.do/index.php/tarjetas-de-credito-mastercard-local'],
                'platinum':['http://www.progreso.com.do/index.php/tarjetas-de-credito-mastercard-platinum-internacional'],
                'platinum card':['http://www.americanexpress.com.do/platinum/priority.html',
                                 'http://www.americanexpress.com.do/platinum/vip.html',
                                 'http://www.americanexpress.com.do/platinum/lifestyle.html',
                                 'http://www.americanexpress.com.do/platinum/rewards.html',
                                 'http://www.americanexpress.com.do/platinum/protection.html',
                                 'http://www.americanexpress.com.do/platinum/cardmember_services.html']}

        path = {'casa de campo':['div','overview_all_data'],
                'american express':['div','overview_all_data'],
                'american express gold':['div','row','class'],
                'suma ccn':['div','overview_all_data'],
                'gold':['table','contentpaneopen','class'],
                'internacional':['table','contentpaneopen','class'],
                'local':['table','contentpaneopen','class'],
                'platinum':['table','contentpaneopen','class'],
                'platinum card':['div','PlatinumContentMain','id']}

        diferentes = ['american express gold','gold','internacional','local','platinum','platinum card']
        if tarjeta in diferentes:
            if tarjeta == 'american express gold':
                tree = ['div','benefits-container','id']
            elif tarjeta == 'platinum card':
                tree = ['div','ContentFeature','id']
            else:
                tree = ['div','mainbody','id']
    if banco == 'ACAP':
        tree = ['div','item-page clearfix','class']
        link = {'gold':['https://www.acap.com.do/site2/index.php/banca-personal/tarjeta-de-credito/tarjeta-de-credito-visa-gold'],
                'clasica':['https://www.acap.com.do/site2/index.php/banca-personal/tarjeta-de-credito/visa-clasica-local'],
                'clasica internacional':['https://www.acap.com.do/site2/index.php/banca-personal/tarjeta-de-credito/visa-clasica-internacional']}

        path = {'gold':['ul','ja-unordered-list'],
                'clasica':['ul','ja-unordered-list'],
                'clasica internacional':['ul','ja-unordered-list']}

    if banco == 'ALNAP':
        tree = ['div','article-content','class']
        link = {'clasica local':['http://www.alnap.com.do/productos/personas/tarjetas/clasica-local'],
                'clasica internacional':['http://www.alnap.com.do/productos/personas/tarjetas/tarjeta-clasica-internacional'],
                'gold':['http://www.alnap.com.do/productos/personas/tarjetas/tarjeta-de-credito-gold'],
                'confiamas':['http://www.alnap.com.do/productos/tarjeta-de-credito-confiamas'],
                'confia en ti local':['http://www.alnap.com.do/productos/confia-en-ti'],
                'confia en ti internacional':['http://www.alnap.com.do/productos/confia-en-ti'],
                'unase local':['http://www.alnap.com.do/productos/personas/tarjetas/tarjeta-visa-unase'],
                'unase internacional':['http://www.alnap.com.do/productos/tarjeta-visa-unase-internacional'],
                'union local':['http://www.alnap.com.do/productos/tarjeta-visa-union'],
                'union internacional':['http://www.alnap.com.do/productos/tarjeta-visa-union'],
                'compramas':['http://www.alnap.com.do/productos/personas/tarjetas/compramas']
                }

        path = {'clasica local':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'clasica internacional':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'gold':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'confiamas':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'confia en ti local':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'confia en ti internacional':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'unase local':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'unase internacional':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'union local':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'union internacional':['div','field field-name-field-content-tab field-type-text-long field-label-hidden'],
                'compramas':['div','field field-name-field-content-tab field-type-text-long field-label-hidden']
                }

    if banco == 'BDI':
        tree = ['div','component-content','class']
        link = {'local':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/tarjetas-visa-bdi'],
                'clasica':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/tarjetas-visa-bdi'],
                'gold':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/tarjetas-visa-bdi'],
                'signature':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/tarjeta-signature'],
                'anthonys clasica':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/tarjeta-anthony-s'],
                'anthonys gold':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/tarjeta-anthony-s'],
                'anthonys platinum':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/tarjeta-anthony-s'],
                'signature bm cargo':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/bmcargo'],
                'crediplan':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/credito-diferido'],
                'bm cargo local':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/bmcargo'],
                'bm cargo clasica':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/bmcargo'],
                'bm cargo gold':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/bmcargo'],
                'fundapec clasica':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/tarjeta-fundapec'],
                'plaza central clasica':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/plaza-central'],
                'plaza central local':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/plaza-central'],
                'plaza central gold':['https://www.bdi.com.do/index.php/productos-y-servicios/tarjetas-de-credito/visa-marca-compartida/plaza-central']
                }

        path = {'local':['article','item-page'],
                'clasica':['article','item-page'],
                'gold':['article','item-page'],
                'signature':['article','item-page'],
                'anthonys clasica':['article','item-page'],
                'anthonys gold':['article','item-page'],
                'anthonys platinum':['article','item-page'],
                'signature bm cargo':['article','item-page'],
                'crediplan':['article','item-page'],
                'bm cargo local':['article','item-page'],
                'bm cargo clasica':['article','item-page'],
                'bm cargo gold':['article','item-page'],
                'fundapec clasica':['article','item-page'],
                'plaza central clasica':['article','item-page'],
                'plaza central local':['article','item-page'],
                'plaza central gold':['article','item-page']
                }
                
    if banco == 'Scotiabank':
        tree = ['div','a overview content','class']
        link = {'scotiabank gold visa':['http://www.scotiabank.com/do/es/0,,6986,00.html','http://www.scotiabank.com/do/es/0,,6988,00.html'],
                'scotiabank mastercard':['http://www.scotiabank.com/do/es/0,,6985,00.html'],
                'scotiabank visa':['http://www.scotiabank.com/do/es/0,,6987,00.html'],
                'scotiabank platinum visa':['http://www.scotiabank.com/do/es/0,,6991,00.html','http://www.scotiabank.com/do/es/0,,6997,00.html'],
                'scotiabank aadvantage visa':['http://www.scotiabank.com/do/es/0,,6992,00.html'],
                'scotiabank aadvantage gold mastercard':['http://www.scotiabank.com/do/es/0,,6993,00.html','http://www.scotiabank.com/do/es/0,,6994,00.html'],
                'scotiabank aadvantage platinum visa':['http://www.scotiabank.com/do/es/0,,6995,00.html'],
                'scotiabank pricesmart diamond mastercard':['http://www.scotiabank.com/do/es/0,,6996,00.html'],
                'scotiabank bravo visa':['http://www.scotiabank.com/do/es/0,,7154,00.html'],
                'scotiabank orange mastercard':['http://www.scotiabank.com/do/es/0,,7155,00.html'],
                'scotiabank visa infinite':['http://www.scotiabank.com/do/es/0,,9492,00.html']}

        path = {'scotiabank gold visa':['div','bullets'],
                'scotiabank mastercard':['div','bullets'],
                'scotiabank visa':['div','bullets'],
                'scotiabank platinum visa':['div','bullets'],
                'scotiabank aadvantage visa':['div','bullets'],
                'scotiabank aadvantage gold mastercard':['div','bullets'],
                'scotiabank aadvantage platinum visa':['div','bullets'],
                'scotiabank pricesmart diamond mastercard':['div','bullets'],
                'scotiabank bravo visa':['div','bullets'],
                'scotiabank orange mastercard':['div','bullets'],
                'scotiabank visa infinite':['div','bullets']}

    if banco == 'BanReservas':
        tree = ['div','beneficios-previews cms-content','class']
        link = {'visa / mastercard / mastercard multimoneda gold':['https://www.banreservas.com/products/visa-y-mastercard-gold'],
                'mastercard platinum':['https://www.banreservas.com/products/mastercard-platinum'],
                'visa clasica y mastercard standard':['https://www.banreservas.com/products/visa-clasica-y-mastercard-standard'],
                'visa y mastercard multimoneda':['https://www.banreservas.com/products/visa-y-mastercard-multimoneda'],
                'visa platinum universe':['https://www.banreservas.com/products/visa-platinum-universe'],
                'visa infinite':['https://www.banreservas.com/products/visa-infinite']}
        
        path = {'visa / mastercard / mastercard multimoneda gold':['div','beneficios-preview'],
                'mastercard platinum':['div','beneficios-preview'],
                'visa clasica y mastercard standard':['div','beneficios-preview'],
                'visa y mastercard multimoneda':['div','beneficios-preview'],
                'visa platinum universe':['div','beneficios-preview'],
                'visa infinite':['div','beneficios-preview']}

    if banco == 'SantaCruz':
        tree = ['div','article-content','class']
        link = {'clasica':['https://www.bsc.com.do/~bsccom/soluciones-personales/tarjetas/tarjetas-de-credito/tarjeta-de-credito-clasica/'],
                'oro':['https://www.bsc.com.do/~bsccom/soluciones-personales/tarjetas/tarjetas-de-credito/tarjeta-de-credito-gold/'],
                'platinum':['https://www.bsc.com.do/~bsccom/soluciones-personales/tarjetas/tarjetas-de-credito/tarjeta-de-credito-platinum/'],
                'infinite':['https://www.bsc.com.do/~bsccom/soluciones-personales/tarjetas/tarjeta-de-credito-infinite/'],
                'multicredito':['https://www.bsc.com.do/~bsccom/soluciones-personales/tarjetas/multicredito/'],
                'full car':['https://www.bsc.com.do/~bsccom/soluciones-personales/tarjetas/full-car/'],
                'cecomsa':['https://www.bsc.com.do/~bsccom/soluciones-personales/tarjetas/tarjeta-cecomsa/']}

        path = {'clasica':['div','entry-body'],
                'oro':['div','entry-body'],
                'platinum':['div','entry-body'],
                'infinite':['div','entry-body'],
                'multicredito':['div','entry-body'],
                'full car':['div','entry-body'],
                'cecomsa':['div','entry-body']}

    if banco == 'BHD':
        tree = ['div','tab_container','class']
        link = {'clasica local':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVNdb4IwFP0r-uAjacUi9ZHsy80tJLBN6YsphWodtAgdbv_eu2XLnpQshr60zT33nJObexBDK8Q0b9WGW2U0L-CfsOmazK7xPSHjxd38FuPAffRmcRRGV3OCXhFDTGhb2S1K0m02wkorocwIp1wLPqjyugGmEba83uWWN38vUeeZsoCsapO9C2ugxp1Bqxo-EAVvFLQXRoALkKiEylBCpz7x6TRzJjijDqEydaiU0uEUS-lKV4zdMVp2eWZQxidOgKGffUNOMCxirwMQ_gLOiCRg0j9t0kfLVuUH9KJNXcIE4n_OYN6lMHMvVOig9_qkd0O_V3pCLqR_OLcfXysIuVK7_Z4FEB6jbf5h0aqv9FRlSSefzltED89yuynXTzcT7-cqNsPhEX567X4!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'standard local':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVPLbsIwEPwVOHCMbBInJMeoL1paIUFbiC_I3hhiSuzguND-fU3VqqcQVSi-eK0dz4xWO4iiJaKKHeSGWakV27l3RqMVSa7xPSHDyd34FuPUfwyT-Ww6uxoT9IoooqBsZQuU8SIfYKkkSD3AnClgvUqY2jENsGVmKyyr_yowIpfWISuj83ew2vW41ytZbYUBZvJebZnKT8VOgzPjlCqQOcoA-xh8HnsBF7FHOAQeB8BePOQR40G0DhOBFm3WqWvjhpNi959-QxoYJvOwBTD9BZwRyZzJUbPJEVocpDiiF6VN6SYw_-cMxm0KiX-hQgt92CW9Px11Sk_IhfQP5_bjtIIuXnK739PUZUgrKz4sWnYcoqos4-DTe5vFx-d1sSlXTzdB-HPtNv3-F1d2JtI!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'clasica premia':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVNdb4IwFP0r-OAjaYFi5ZHsy80tJLBN6Yu5lKJ1UrB0uv371WXLnpQsxr60zT33nJP2HsTQHDEFO7kEIxsFG3vP2WhBomt8T4g3vZvcYhz7j2GUpUl6NSHoFTHEuDKtWaG8WJVDLJXkshniAhQHpxW6s0xDbECvhYHu78S1KKWxyFY35Ts3ja1x19nJDhy-gU4e2rWoJRw0Wi5LlHs4qGhVFi6MKLjEp4Vb0CpygxCL0IcKe7RAsz7TzJbxkRVj28--IUcYplnYA0h-ASdEcmuSHjdJ0WwnxR69qEbX9iOyf77BpE8h8s9U6KEPL0nvJ_Si9IScSf9waj4OI2iDJdfbLYttehplxIdB84vFp63rcfDpvqXj_XO1WtaLp5sg_Nk2y8HgCz2JFF0!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'clasica internacional':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVPLbsIwEPwVOORo2TUOSY6or7S0QoK2EF-QH0kwJU5IXGj_nu1LPUFUofhiWzs7M1rNYo4XmFuxM7lwprRiA_-ED5csuiJ3jF2Mb-MbQkb0wY9m08n0Mmb4BXPMlXWVW-FErrRHjDXKlB6RwirRq9K6ASaPOFGvUyeav5eqU20cIKu61G_KlVDTqLczjeipjWgMtBvr0toK9e0GpCplNE40i6gMpUYi0xliQkkUDiOKMhYwGko_iIjG8zbvHMrkyBkR6OdfkCMM45nfApj8Ak6IJGAyOG4ywPOdSff42ZZ1AROY_XMGcZtCRM9UaKH3u6Snk6BTesbOpL8_lY_PCMJ-mfV2y0ewRCVk_d3hRddbVBVFOPhAr9Nw_5St8mL5eD3wf65N3u8fAIh6K2o!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'standard internacional':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/vVPLbsIwEPwVOHCMbBIHkyPqi5ZWSNAW4gtabAOmxAmOC-3fd-lDPYWoQtQXr73jmfVqlggyJcLCzizBm9zCBs-p6MxYcklvGWsPbvrXlPbC-zgZj4ajiz4jz0QQIa0v_Iqk85VqUWONNHmLzsFKaBTalcjUoh7cWnsofyPptDIekYXL1av0OeZ00Mig9NpJcKpRerDqEBiLVxbkV1GoWEijSBpG7XaXdniwYKEKGHSSAGIJwUJFHPg84TpWZFL3BYFpWrF6FN-LT0gFw2Ac1wCGP4AjIikWyauL5GSyM3pPnmzuMuzA-I896NcpJOGJCjX08TnpwyE_Kz1jJ9LfHfPHwYI4Zma93YoezlKOXn_zZPpPw1RkWTd6D15G3f3jYrXMZg9XUfy9bZbN5gdcBKLW/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'mi pais':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tZNdb8IgFIb_Sr3wsgFbOuSy2Vc3tzTRbVpuDAXa4izUlun274fLll1pszi5gZPz8rwncA6gYAGoZltVMquMZmsXZ_RiicgVvENoNLlNbiCMg4eIzKbp9DJB4AVQQLm2ja1AlldiCJVWXJkhzJnmzGtk2znSEFrWrqRl3e-Jt1Io65RNa8Qbt8blCt_bqo55tfIapro9vOFKgAwiIfE4Zz4PRpGPMMQ-gYT5IoQ5KaQg4agA875qqUvDAyuG7j79khwgTGZRjyD9ERwxyVyR-HCRGMy3Su7AszZt7X5g9sc3SPocSHCiQw8-Oic-SPFZ8QidiL8_1h_7FnQTpVabDY3d2Bht5bsFi_-fm6aux-GH_zod756KqqyXj9dh9L2ty8HgEwp3v34!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'gold internacional':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tZNdT4MwFIb_CrvgkrR2ZcAl8Ws6zZKhbvRmKW2FTmgZVKb_fp3ReMWImetNe3LePufNyTmAgBUginYyp0ZqRUsbp2SyxtEVvMP4YnY7vYEwRg9-lCzmi8spBi-AAMKUqU0B0qzgLpRKMqldmFHFqFOLprUkFxrabISh7e-LNYJLY5V1o_k7M9rmCs_pZEudXJf8QK6Z5CBFEcIiRJGHeUY9a4R7kc-QFwrGJihj_iTLwHLIKrFp2HNiaP-TL0kPYZb4A4L5j-BIkdSaDPpNBmDZSbEDz0o3lW1_8sceTIcqROjECgN4_5x4NA_Oisf4RPz9sfk4jKBdJ7nZbklsd0YrIz4MWP3z0tRVFY4_vbdFuHt6LfJq_Xg99r-vMh-N9pNYYm4!/dz/d5/L2dBISEvZ0FBIS9nQSEh/','https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tZPLbsIwEEV_BRYsLbvEeS1RX2lphQRtId4gv0hMEzsYF9q_x1StuoKoQvHGHs31uSN7BhK4gETTnSqoU0bTysc5iZY4vUEPGF-N77M7hEbDpzCdTSfT6wzDN0gg4do1roQ5K8UAKa24MgPEqOa010i79aQBctSupaPbvxO3UijnlY014oM743MK9Gq6ddJyakWvMJU48huuBMyTgDMWRTGgIUMAYy4BQ3EKIiHCBEUJ4sEKztsKJj6NTqwR8vfJt-QEYTwLWwSTX8EZk9wXGZ8uMobznZJ7-KqNrf0nzP75BlmbQzq80KEFH3aJH07iTvEYX4h_PNcfxxb0Q6XWmw0Z-ckx2slPBxedjE5T10nwBd6nyf5lVRb18vk2CH-2quj3Dwq5ONc!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'gold mujer':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVNdb8IgFP0r9cHHBtbSlj6afbm5pUndh-XFUMBK10JF1O3fi8uWPWmzGHngI_fccy5wDyBgBoiiW1lRK7WijTsXJJ6j9AY-IHQ1uR_fQTgKnqJ0mmf59RiBN0AAYcp2dgmKcsmHUCrJpB7CkipGvU6YtWMaQktNLSxd_-2YEVxah-yM5htmtYvVvtfStRWGUcO9Sjfcaze1MAeVjkkOijRKwzKOY7_EZeCjgKc-5m4KMcbxgpUMRgl47yubuDA8MkbQ5ZNvyBGGyTTqAWS_gBMihSsyOV6ku8VWih14Vdq07ium_3yDcZ9CGpyp0EMfXZI-yJKL0iN0Jv3jqf44tKCzlqxXKzJy_tHKik8LZhc0UNe2OPzyP3K8e1ksq3b-fBtGP0tTDQZ76p2o8g!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'gold premia':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tZNdb4IwFIb_Cl54SVqhfF2afbG5hQS2qb0xpS1QhRah0-3fW5ctu1KyGHvTnpy3z3vSngMwWAAsyU6URAslSW3iJfZXKLqFjwhNZg_xPYRT59mLsjRJb2IE3gEGmErd6gos84qNoZCCCjWGOZGUWC3vekMaQ026Ndek_zvRjjOhjbLtFPugWpncxrZ2oidWqWpmtR1vBDkatFQwgy-gDylnNstDZiM3D2wCaWQXnBRBOGEu8RmYD1WMTRqeWFNo7uNvyQnCLPMGBMmv4IzJ0hQZnC4yAPOd4HvwJlXXmF_I_vkG8ZBD5FzoMID3rol3kuCqeIQuxD-d649jC5qpEuvtFk_N6Cip-acGi-vMTts0oftlb9Jw_1pUZbN6uXO9n60uR6MDGp_Hpw!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'mlb':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVPLbsIwEPyVcOAY2QSnSY5RX7S0QoK2EF_Q-kEwTexgXGj_HlO16gmiCuGLvdrxzMjeQRTNENWwVSU4ZTRUvi7o1ZxkN_iBkN7wfnCHcR49xdlkPBpfDwh6QxRRrl3jlqhgS9HFSiuuTBcz0ByCRtqNZ-piB3YlHWz-TtxKoZxHNtaID-6M71VhUMPGScvBiqA0lQjqih00Gq4EKhKcAunzRdhLGQ4JEBICExBGLMO9LJYZi2I0bTNNfRsfWTn29-k35AjDcBK3AEa_gBMihTeZHDeZoOlWyR161cbW_iMm_3yDQZtCFp2p0EIfX5I-GiUXpSfkTPrHU_NxGEEfLLVar2nu02O0k58OzS4Wn6au0_5X-D5Ody-LZVnPn2_78c9WlZ3OHrsfpoM!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'beisbol invernal':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/vVNbT8IwGP0r44FEH5Z2o2Pb4-INRUMCKqwvpDehuLajq6D_3mI0PsFiCPalbb7Tc07b7wAMZgBrspEL4qTRpPL7EvfnKL-EtwhFw5vBNYRFfJ_kk_FofDFA4BlggJl2tVuCki55F0otmTRdSIlmJKiFbTxTFzpiV8KR5nfFrODSeWRtDX9jzviaCgNFGicsI5YHVMiGmiqQeiOstxOcVZIbdb7TrJnkoOyjGKZRLw4zSlGIBExDmjAYpjDLeIRYLPIITNsugX0Z7hkF9OfxF2QPw3CStABGP4ADIqU3me43mYLpRooteNLGKv8xkz--waBNIY-PVGihT05JH4_Sk9IjdCT93aH-2LWgD5pcrde48Gky2ol3B2b_Fqdaqaz3Eb6Os-3jy3Kh5g9XveR7qhadzieykykF/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'platinum':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tZNdb4IwFIb_il5wSVqgKFySfbG5xQS3Kb0xtRSog4JQdfv3Hpctu0KyGHrTnpy3z3nTnoMoWiGq2EFmTMtKsQLimE7WxL_Fj4RYs4fwHuPAfnb9RTSPbkKC3hFFlCtd6xzFmzwxsFSSy8rAG6Y4G9WiaYFkYM2ardCs_TvxRiRSg7JuqmTPdQW52hwdZAvXCnCg9uWZXnOZoNifJI5lW64pEj81icMtk6UCQ8i81MeejW0XLfvsUkjjjhVguE-_JR2E2cLtEcx_BReKxGBy2m1yipYHKY7oTVVNCV-w-OcbhH0VfPvKCj14d0i8PZ8OiifkSvzTpf44tyCMlNzudjSAuamUFp8arQYYnLosPefL_Ii842uaZ-X65c5xf7YiG49PbZqOlg!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'black mujer':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVNdb4IwFP0r-OAjacEy4JHsi80tJrpN6Yu5tEWqUrBU3f69ddmyJyWLsS_tzT0956S9B1E0Q1TBTi7AyFrB2tYZvZmT-A4_EeINH9MHjBP_JYgn49H4NiXoA1FEmTKNKVGWl7yPpZJM1n2cg2LgNEK3lqmPDeilMND-nZgWXBqLbHTNt8zUtte6TgWtEZqB5k6-BrZyqu1S6KNMwyRHmQARe14IbhRD4RIfQjcqAnB9zrzIw0U-iDmadvmmto1PrATb-_QbcoJhOAk6AKNfwBmRzJoMT5sM0XQnxR69q1pX9i8m_3yDtEsh9i9U6KAPrknvj8Kr0hNyIf3zufk4jqDNllxuNjSxAaqVEZ8Gza6ZoKaqosGXuxpH-7eiXFTz1_tB8LOtF73eAeIg9ag!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'siremas oro':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVNbb4IwGP0r-OAjacEi8Eh2Y3MLCW5T-mJKqVAnLZaK27-3Llv2hGQx9qGXfKfnnLTfARgsARak4yXRXAqyNecMT1covIWPCDmzh_gewsh99sJ5mqQ3MQLvAANMhW50BbK8KsaQC065HMOcCEqshqnWMI2hJmrDNGn_dlSxgmuDbJQs9lRLU9vbVsdbYrVcsZq0llTyJNBQXoDMcdnUgfnaJqcJEeLZgZO7NoQBoiHLc8ehYDHkGJsy7BkRNPfxN6SHYTb3BgDJL-CMSGZM-v0mfbDoODuANyFVbX5h_s83iIcUQvdChQF675r0buJflR6hC-mfzvXHqQVNqvhmt8ORiY4Umn1qsLxOdpq6DiZf9kcaHF7XVVmvXu4m3s-yLUejI-t56Fk!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'la cadena':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tZNdb4IwFIb_Cl54SVqhFbgk-3JzC4luU3pjjm3ROiiIHW7_fnXZsiski6E37cl5-7wn7TmIoSViGhq1AaNKDbmNUzZekega3xMymt5NbjGOvUcazWfJ7GpC0CtiiHFtKrNF6XorhlhpxVU5xGvQHJxK1gdLGmID9U4aOPydeC2FMlZZ1aV456Y85VynUQdwcnA4CKnhhK-4EiglYhSCBHDDMPBdkvmeG0V07GKfg59RKnjmoUVXvcymccuKsb3PviUthOmcdgiSX8EZk9QWGbQXGaBFo-QRveiyLuwfzP_5BpMuh8i70KEDT_vEe0nQK56QC_EP5_rj1IJ2ptRuv2exHZxSG_lh0LKPyamKIvQ_3bdZeHzOtpti9XTj058t3wwGX0IaDcs!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'platinum mujer':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tVNdb8IgFP0r9cHHBqS0lcdmX93cYqLbtLwYStHihFaKuv17cdmyJ20WU17g5h7OOYF7AAVzQDXbyxWzstJs4-qMRgtMbuEjxoPRQ3oPYYKeQzKdjCc3KQbvgALKta1tCbK8LPpQasll1Yc505x5tTCNY-pDy8xaWNb8nbgRhbQOWZuq2HFbud7W9xRrrDCcmcKrN86H3ilP7dbCnJRqLguQBWQpch5HPonjwMcCcT8vlsIfBBFCIiQkGiAwa7NOXRueWQl09-k35AzDaBq2AMa_gAsimTMZnzcZg9leigN405VR7jum_3yDtE2BoCsVWujDLunROO6UHuMr6Z8uzcdpBF285Hq7pYnLUKWt-LRg3nGIaqWGwZf_MRkeXpflSi1e7oLwZ9user0j9HdKRQ!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/'],
                'infinite':['https://www.bhdleon.com.do/wps/portal/BHD/Inicio/bancapersona/Productos/!ut/p/z1/tZNdT4MwFIb_CrvgkrRCkfaS-IVOQwLqRm-WjnbQOQqDyvTf2xmNV4yYhd60J-ft85605wAKloAq1suCaVkrtjNxRi9XiFzDe4Qu5nfRLYSh--iTNImTqwiBV0ABzZVudAmydcltKJXMZW3DNVM5sxrRdoZkQ83ardCs-zvlreBSG2XT1vw917XJtY7Vy45ZUm0MR4sjvcklBxn3XA4ZYo6HA99BGHoOI4Q43IUIC1cIQTBYjJVLTRoOrBCa-_RbMkCYp_6IIP4VnDDJTJHBcJEBWPRSHMCLqtvKfEH6zzeIxhyIe6bDCN6fEu_GwaR4hM7EP5zqj2MLmpGS2_2ehmZuaqXFhwbLCQanqSrsfTpvCT48b8qiWj3deP7Ptitmsy-IVfzf/dz/d5/L2dBISEvZ0FBIS9nQSEh/']
                }

        path = {'clasica local':['div','tab2','id'],
                'standard local':['div','tab2','id'],
                'clasica premia':['div','tab2','id'],
                'clasica internacional':['div','tab2','id'],
                'standard internacional':['div','tab2','id'],
                'mi pais':['div','tab2','id'],
                'gold internacional':['div','tab2','id'],
                'gold mujer':['div','tab2','id'],
                'gold premia':['div','tab2','id'],
                'mlb':['div','tab2','id'],
                'beisbol invernal':['div','tab2','id'],
                'platinum':['div','tab2','id'],
                'black mujer':['div','tab2','id'],
                'siremas oro':['div','tab2','id'],
                'la cadena':['div','tab2','id'],
                'platinum mujer':['div','tab2','id'],
                'infinite':['div','tab2','id']
                }

    if banco == 'Bancamerica':
        tree = ['section','beneficio','class']
        link = {'clasica':['http://bancamerica.com.do/banca_personal/visa_clsica_bancamrica'],
                'gold':['http://bancamerica.com.do/banca_personal/visa_gold_bancamrica'],
                'platinum':['http://bancamerica.com.do/banca_personal/visa_platinum_bancamrica'],
                'signature':['http://bancamerica.com.do/banca_personal/visa_signature_bancamrica']}

        path = {'clasica':['div','container'],
                'platinum':['div','container'],
                'gold':['div','container'],
                'signature':['div','container']
                }

    if banco == 'Vimenca':
        c = {'clasica local':'clasica-local',
             'clasica int':'clasica-internacional',
             'gold':'gold-internacional',
             'black gold':'black-gold-internacional',
             'platinum':'platinum-internacional',
             'gold pagatodo':'gold-pagatodo'}
        tree = ['div','yoo-zoo blog-uikit blog-uikit-tarjeta-de-credito-visa-'+c[tarjeta],'class']
        link = {'clasica int':['http://www.bancovimenca.com/portal/tarjetas/tarjeta-de-credito-visa-clasica-internacional'],
                'clasica local':['http://www.bancovimenca.com/portal/tarjetas/tarjeta-de-credito-visa-clasica-local'],
                'gold':['http://www.bancovimenca.com/portal/tarjetas/tarjeta-de-credito-visa-gold-internacional'],
                'black gold':['http://www.bancovimenca.com/portal/tarjetas/tarjeta-de-credito-visa-black-gold-internacional'],
                'platinum':['http://www.bancovimenca.com/portal/tarjetas/tarjeta-de-credito-visa-platinum-internacional']}

        path = {'clasica int':['article','uk-article'],
                'clasica local':['article','uk-article'],
                'gold':['article','uk-article'],
                'black gold':['article','uk-article'],
                'platinum':['article','uk-article']}

    if banco == 'Promerica':
        tree = ['div','entrytext','class']
        link = {'platinum':['Promerica-visa'],
                'spirit gold':['Promerica-mastercard'],
                'spirit platinum':['Promerica-mastercard'],
                'lama plazos clasica':['Promerica-visa'],
                'platinum premium':['Promerica-visa'],
                'infinite':['Promerica-visa'],
                'gold':['Promerica-visa'],
                'mi super clasica':['Promerica-visa']}

        path = {'platinum':['div','collapseomatic'],
                'spirit gold':['div','collapseomatic'],
                'spirit platinum':['div','collapseomatic'],
                'lama plazos clasica':['div','collapseomatic'],
                'platinum premium':['div','collapseomatic'],
                'infinite':['div','collapseomatic'],
                'gold':['div','collapseomatic'],
                'mi super clasica':['div','collapseomatic']}

    if banco == 'Caribe':
        tree = ['div','panel-grid-cell','class']
        link = {'elite':['http://www.bancocaribe.com.do/personas/visa-elite/'],
                'platinum':['http://www.bancocaribe.com.do/personas/tarjetas-de-credito-general/platinum/'],
                'oro local':['http://www.bancocaribe.com.do/personas/visa-oro/'],
                'clasica local':['http://www.bancocaribe.com.do/personas/tarjetas-de-credito-general/visa-clasica/'],
                'clasica internacional':['http://www.bancocaribe.com.do/personas/tarjetas-de-credito-general/visa-clasica/'],
                'card':['http://www.bancocaribe.com.do/personas/ecard/']
                }

        path = {'elite':['div','textwidget'],
                'platinum':['div','textwidget'],
                'oro local':['div','textwidget'],
                'clasica local':['div','textwidget'],
                'clasica internacional':['div','textwidget'],
                'card':['div','textwidget']
                }

    if banco == 'APAP':
        tree = ['div','content','id']
        link = {'clasica internacional':['http://www.apap.com.do/views/personas-familias/visa.aspx'],
                'clasica local':['http://www.apap.com.do/views/personas-familias/visa.aspx'],
                'gold ':['http://www.apap.com.do/views/personas-familias/visa.aspx'],
                'gold':['http://www.apap.com.do/views/personas-familias/mastercard.aspx'],
                'standard local':['http://www.apap.com.do/views/personas-familias/mastercard.aspx'],
                'standard internacional':['http://www.apap.com.do/views/personas-familias/mastercard.aspx'],
                'platinum':['http://www.apap.com.do/views/personas-familias/platinum.aspx'],
                'familiar':['http://www.apap.com.do/views/personas-familias/tarjetas-familiar.aspx']
                }

        path = {'clasica internacional':['div','col w5','class'],
                'clasica local':['div','col w5','class'],
                'gold ':['div','col w5','class'],
                'gold':['div','col w5','class'],
                'standard local':['div','col w5','class'],
                'standard internacional':['div','col w5','class'],
                'platinum':['div','col w10','class'],
                'familiar':['div','col w10','class']
                }

    return (link.get(tarjeta),path.get(tarjeta),tree)

def obtener_beneficios(urls,path,tree,otros=None):
    if not urls or len(urls) == 0:
        return ''
    final = ''
    for url in urls:
        # Realizamos la petición a la web
        #req = urllib.urlopen(url)
        opener = MyOpener()
        req = opener.open(url)
        x = req.read()
        resultado = []
        # Comprobamos que la petición nos devuelve un Status Code = 200
        statusCode = req.getcode()
        if statusCode == 200:

            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(x)
            #b = {}
            # Obtenemos todos los divs donde estan las entradas
            entradas = html.find_all(tree[0],{tree[2] : tree[1]})
            b = ''

            # Recorremos todas las entradas para extraer el título, autor y fecha
            for i,entrada in enumerate(entradas):
                #a = []
                a = ''
                # Con el método "getText()" no nos devuelve el HTML
                if len(path) == 3:
                    titulo = entrada.find_all(path[0], {path[2] : path[1]})
                else:
                    titulo = entrada.find_all(path[0], {tree[2] : path[1]})
                for e in titulo:
                    a = a+"%s"%e.getText()
                if otros:
                    datos = html.find_all(otros[0],{tree[2]: otros[1]})
                    for s in datos:
                        if len(s.getText().split())<10:
                            resultado.append(limpiar(s.getText()))
                    tarjeta = otros[2]
                # Sino llamamos al método "getText()" nos devuelve también el HTML
                #autor = entrada.find('span', {'class' : 'autor'})
                #fecha = entrada.find('span', {'class' : 'fecha'}).getText()
                if i == 0:
                    b = a

                # Imprimo el Título, Autor y Fecha de las entradas
               # print ("%d - %s  |  %s  |  %s" %(i+1,titulo,autor,fecha))
                while '' in resultado:
                    resultado.remove('')
                if otros:
                    b = mas_beneficios(b,a,resultado,i,tarjeta)
                #.encode('utf-8').replace("\xc1","A").replace("\xe1","a").replace("\xc9","E").replace("\xe9","e").replace("\xcd","I").replace("\xed","i").replace("\xd3","O").replace("\xf3","o").replace("\xda","U").replace("\xfa","u").replace("\xd1","N").replace("\xf1","n")
                #.replace('\n','').replace('\r','')

        else:
            return "Status Code %d : %s" %(statusCode,req.read())
        final += b
    if final:
        return final.replace('<!--','').replace('-->','').replace('<strong>','').replace('</strong','')
    else:
        return 'No se encuentran beneficios.'

def mas_beneficios(b,a,resultado,i,tarjeta):
    boolean = False
    if len(resultado)>0:
        for e in resultado[i-1].lower().split():
            if e in tarjeta:
                boolean += 1
            if boolean > len(resultado[i-1].lower().split())-2:
                return a+b
        return b
    else:
        return b+a

def obtener_beneficios_promerica(urls,path,tree,otros):
    if not urls or len(urls) == 0:
        return ''
    final = ''
    for url in urls:
        resultado = []
        html = BeautifulSoup(open('html/'+url+'.html'))
        entradas = html.find_all(otros[0],{tree[2] : otros[1]})
        b = ''
        a = []
        for i,entrada in enumerate(entradas):
            for z in otros[2].split():
                if z in entrada.getText().lower():
                    b = entrada.find_next_sibling('div').getText()
                    break
                    break
        return b
    return None
from bs4 import BeautifulSoup as BS
import pyperclip
def test_pro(url='http://signup-12.appspot.com/test1'):
    req = urllib2.urlopen(url).read()
    pyperclip.copy(req)
    html1 = BS(open('html/Promerica-visa.html').read())
    html = BS('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- saved from url=(0041)http://www.promerica.com.do/?page_id=4002 -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
<title>Banco Promerica – Tarjetas Visa</title>
<link rel="stylesheet" href="./test_files/style.css" type="text/css" media="screen">
<link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="http://www.promerica.com.do/?feed=rss2">
<link rel="pingback" href="http://www.promerica.com.do/xmlrpc.php">
<meta name="generator" content="WordPress 4.7.3"> <!-- leave this for stats -->
<link rel="dns-prefetch" href="http://assets.juicer.io/">
<link rel="dns-prefetch" href="http://maxcdn.bootstrapcdn.com/">
<link rel="dns-prefetch" href="http://s.w.org/">
        <script type="text/javascript">
            window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.2.1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.2.1\/svg\/","svgExt":".svg","source":{"concatemoji":"http:\/\/www.promerica.com.do\/wp-includes\/js\/wp-emoji-release.min.js?ver=4.7.3"}};
            !function(a,b,c){function d(a){var b,c,d,e,f=String.fromCharCode;if(!k||!k.fillText)return!1;switch(k.clearRect(0,0,j.width,j.height),k.textBaseline="top",k.font="600 32px Arial",a){case"flag":return k.fillText(f(55356,56826,55356,56819),0,0),!(j.toDataURL().length<3e3)&&(k.clearRect(0,0,j.width,j.height),k.fillText(f(55356,57331,65039,8205,55356,57096),0,0),b=j.toDataURL(),k.clearRect(0,0,j.width,j.height),k.fillText(f(55356,57331,55356,57096),0,0),c=j.toDataURL(),b!==c);case"emoji4":return k.fillText(f(55357,56425,55356,57341,8205,55357,56507),0,0),d=j.toDataURL(),k.clearRect(0,0,j.width,j.height),k.fillText(f(55357,56425,55356,57341,55357,56507),0,0),e=j.toDataURL(),d!==e}return!1}function e(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var f,g,h,i,j=b.createElement("canvas"),k=j.getContext&&j.getContext("2d");for(i=Array("flag","emoji4"),c.supports={everything:!0,everythingExceptFlag:!0},h=0;h<i.length;h++)c.supports[i[h]]=d(i[h]),c.supports.everything=c.supports.everything&&c.supports[i[h]],"flag"!==i[h]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[i[h]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(g=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",g,!1),a.addEventListener("load",g,!1)):(a.attachEvent("onload",g),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),f=c.source||{},f.concatemoji?e(f.concatemoji):f.wpemoji&&f.twemoji&&(e(f.twemoji),e(f.wpemoji)))}(window,document,window._wpemojiSettings);
        </script>
        <style type="text/css">
img.wp-smiley,
img.emoji {
    display: inline !important;
    border: none !important;
    box-shadow: none !important;
    height: 1em !important;
    width: 1em !important;
    margin: 0 .07em !important;
    vertical-align: -0.1em !important;
    background: none !important;
    padding: 0 !important;
}
</style>
<link rel="stylesheet" id="overlay-basic-css" href="./test_files/overlay-basic.css" type="text/css" media="all">
<link rel="stylesheet" id="juicerstyle-css" href="./test_files/embed.css" type="text/css" media="all">
<link rel="stylesheet" id="dobsondev-shortcodes-css-css" href="./test_files/dobsondev-shortcodes.min.css" type="text/css" media="all">
<link rel="stylesheet" id="dobsondev-shortcodes-font-awesome-css" href="./test_files/font-awesome.min.css" type="text/css" media="all">
<link rel="stylesheet" id="collapseomatic-css-css" href="./test_files/dark_style.css" type="text/css" media="all">
<link rel="stylesheet" id="wpsl-styles-css" href="./test_files/styles.min.css" type="text/css" media="all">
<link rel="stylesheet" id="multilevelnav_style-css" href="./test_files/saved_resource" type="text/css" media="all">
<link rel="stylesheet" id="myStyleSheets-css" href="./test_files/wpcufpn_front.css" type="text/css" media="all">
<link rel="stylesheet" id="myFonts-css" href="./test_files/css" type="text/css" media="all">
<link rel="stylesheet" id="promoslider_main-css" href="./test_files/slider.css" type="text/css" media="all">
<!-- This site uses the Google Analytics by MonsterInsights plugin v6.1.7 - Using Analytics tracking - https://www.monsterinsights.com/ -->
<script type="text/javascript" data-cfasync="false">
    /* Function to detect opted out users */
    function __gaTrackerIsOptedOut() {
        return document.cookie.indexOf(disableStr + '=true') > -1;
    }

    /* Disable tracking if the opt-out cookie exists. */
    var disableStr = 'ga-disable-UA-31048290-1';
    if ( __gaTrackerIsOptedOut() ) {
        window[disableStr] = true;
    }

    /* Opt-out function */
    function __gaTrackerOptout() {
      document.cookie = disableStr + '=true; expires=Thu, 31 Dec 2099 23:59:59 UTC; path=/';
      window[disableStr] = true;
    }

    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','__gaTracker');

    __gaTracker('create', 'UA-31048290-1', 'auto');
    __gaTracker('set', 'forceSSL', true);
    __gaTracker('require', 'displayfeatures');
    __gaTracker('send','pageview');
</script>
<!-- / Google Analytics by MonsterInsights -->
<script type="text/javascript">
/* <![CDATA[ */
window.CKEDITOR_BASEPATH = "http://www.promerica.com.do/wp-content/plugins/ckeditor-for-wordpress/ckeditor/";
var ckeditorSettings = { "textarea_id": "comment", "pluginPath": "http:\/\/www.promerica.com.do\/wp-content\/plugins\/ckeditor-for-wordpress\/", "autostart": true, "excerpt_state": false, "qtransEnabled": false, "outputFormat": { "indent": true, "breakBeforeOpen": true, "breakAfterOpen": true, "breakBeforeClose": true, "breakAfterClose": true }, "configuration": { "height": "160px", "skin": "moono", "scayt_autoStartup": false, "entities": true, "entities_greek": true, "entities_latin": true, "toolbar": "WordpressBasic", "templates_files": [ "http:\/\/www.promerica.com.do\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.templates.js" ], "stylesCombo_stylesSet": "wordpress:http:\/\/www.promerica.com.do\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.styles.js", "allowedContent": true, "customConfig": "http:\/\/www.promerica.com.do\/wp-content\/plugins\/ckeditor-for-wordpress\/ckeditor.config.js" }, "externalPlugins": [  ], "additionalButtons": [  ] }
/* ]]> */
</script><style type="text/css">
            #content table.cke_editor { margin:0; }
            #content table.cke_editor tr td { padding:0;border:0; }
        </style><script type="text/javascript" src="./test_files/jquery.tools.min.wp-front.v3.js.download"></script>
<script type="text/javascript" src="./test_files/jquery.js.download"></script>
<script type="text/javascript" src="./test_files/jquery-migrate.min.js.download"></script>
<script type="text/javascript" src="./test_files/embed-no-jquery.js.download"></script>
<script type="text/javascript" src="./test_files/dobsondev-shortcodes.min.js.download"></script>
<script type="text/javascript" src="./test_files/superfish.js.download"></script>
<script type="text/javascript" src="./test_files/suckerfish_keyboard.js.download"></script>
<script type="text/javascript" src="./test_files/ckeditor.js.download"></script>
<script type="text/javascript" src="./test_files/ckeditor.utils.js.download"></script>
<script type="text/javascript">
/* <![CDATA[ */
var promoslider_options = {"version":"3.3.4"};
/* ]]> */
</script>
<script type="text/javascript" src="./test_files/promoslider.js.download"></script>
<link rel="https://api.w.org/" href="http://www.promerica.com.do/?rest_route=/">
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://www.promerica.com.do/xmlrpc.php?rsd">
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://www.promerica.com.do/wp-includes/wlwmanifest.xml"> 
<meta name="generator" content="WordPress 4.7.3">
<link rel="canonical" href="http://www.promerica.com.do/?page_id=4002">
<link rel="alternate" type="application/json+oembed" href="http://www.promerica.com.do/?rest_route=%2Foembed%2F1.0%2Fembed&amp;url=http%3A%2F%2Fwww.promerica.com.do%2F%3Fpage_id%3D4002">
<link rel="alternate" type="text/xml+oembed" href="http://www.promerica.com.do/?rest_route=%2Foembed%2F1.0%2Fembed&amp;url=http%3A%2F%2Fwww.promerica.com.do%2F%3Fpage_id%3D4002&amp;format=xml">
<link rel="stylesheet" id="fsmlStyleSheet-1-5-1" href="./test_files/fsml-base.css" type="text/css" media="all"><style type="text/css">
        /*disclaimer: this css is php-generated, so while it isnt pretty here it does look fine where its generated*/#fsml_ff, #fsml_ffhidden, #fsml_fblikemodal {
            background-color: #fff; border: 2px solid #ddd; box-shadow: none;border: none;} #fsml_ff, #fsml_ffhidden { right: 0;  top: 50px;} #fsml_fblikemodal { left: -185px; }.fsml_xlr { right: 0; } #fsml_ff { border-radius: 0; }#fsml_ffmain img { border-radius: 0; }#fsml_ff { width: 43px; margin: 0 1%; } .fsml_fflink img, #fsml_twfollow, img#fsml_ytsub { margin-bottom: 3px; }
            @media only screen and (max-width: 800px) {  
                /* hide the floating links frame on small mobile devices in case of overlap issues presented by some themes */
                #fsml_ff {display: none;}
                #fsml_ffhidden {display: none;}
        }#fsml_ff, 
        #fsml_ffhidden {
            opacity: 0.5;
        }
        #fsml_ff:hover, 
        #fsml_ffhidden:hover {
            opacity: 1;
        }/* Grayscale Images */
        #fsml_ff img {
            filter: url(http://www.promerica.com.do/wp-content/plugins/floating-social-media-links/filters.svg#grayscale); /* Firefox 3.5+ */
            filter: gray; /* IE6-9 */
            filter: grayscale(100%); /* Current draft standard */
            -webkit-filter: grayscale(1); /* Old Webkit */
            -webkit-filter: grayscale(100%); /* New WebKit */
            -moz-filter: grayscale(100%); /* Not yet supported in Gecko, Opera or IE */ 
            -ms-filter: grayscale(100%); /* no css solution for IE 10 */
            -o-filter: grayscale(100%); 
        }
        #fsml_ff img:hover {
            filter: none;
            -webkit-filter: grayscale(0);
            -moz-filter: grayscale(0);
            -ms-filter: grayscale(0);
            -o-filter: grayscale(0);
        }/*custom css styling:*/
        </style>
<!-- Multi-level Navigation Plugin v2.3.6 by Ryan Hellyer ... https://geek.hellyer.kiwi/multi-level-navigation/ -->
<!--[if lte IE 7]><script type="text/javascript" src="http://www.promerica.com.do/wp-content/plugins/multi-level-navigation-plugin/scripts/suckerfish_ie.js"></script><![endif]--><script>jQuery(document).ready(function() {
    jQuery("ul.sf-menu").superfish({
        animation:     {opacity:"show",height:"show"},  // fade-in and slide-down animation
        delay:        50,                            // delay on mouseout
        speed:        "slow",  // animation speed
        autoArrows:   "",  // enable generation of arrow mark-up
        dropShadows:  ""  // enable drop shadows
    });
});
/**
* hoverIntent is similar to jQuery's built-in "hover" function except that
* instead of firing the onMouseOver event immediately, hoverIntent checks
* to see if the user's mouse has slowed down (beneath the sensitivity
* threshold) before firing the onMouseOver event.
*
* hoverIntent r5 // 2007.03.27 // jQuery 1.1.2+
* <http://cherne.net/brian/resources/jquery.hoverIntent.html>
*
* hoverIntent is currently available for use in all personal or commercial
* projects under both MIT and GPL licenses. This means that you can choose
* the license that best suits your project, and use it accordingly.
*
* // basic usage (just like .hover) receives onMouseOver and onMouseOut functions
* $("ul li").hoverIntent( showNav , hideNav );
*
* // advanced usage receives configuration object only
* $("ul li").hoverIntent({
*   sensitivity: 7, // number = sensitivity threshold (must be 1 or higher)
*   interval: 100,   // number = milliseconds of polling interval
*   over: showNav,  // function = onMouseOver callback (required)
*   timeout: 0,   // number = milliseconds delay before onMouseOut function call
*   out: hideNav    // function = onMouseOut callback (required)
* });
*
* @param  f  onMouseOver function || An object with configuration options
* @param  g  onMouseOut function  || Nothing (use configuration options object)
* @author    Brian Cherne <brian@cherne.net>
*/
(function($) {
    $.fn.hoverIntent = function(f,g) {
        // default configuration options
        var cfg = {
            sensitivity: 10,
            interval: 150,
            timeout: 0
        };
        // override configuration options with user supplied object
        cfg = $.extend(cfg, g ? { over: f, out: g } : f );

        // instantiate variables
        // cX, cY = current X and Y position of mouse, updated by mousemove event
        // pX, pY = previous X and Y position of mouse, set by mouseover and polling interval
        var cX, cY, pX, pY;

        // A private function for getting mouse position
        var track = function(ev) {
            cX = ev.pageX;
            cY = ev.pageY;
        };

        // A private function for comparing current and previous mouse position
        var compare = function(ev,ob) {
            ob.hoverIntent_t = clearTimeout(ob.hoverIntent_t);
            // compare mouse positions to see if they've crossed the threshold
            if ( ( Math.abs(pX-cX) + Math.abs(pY-cY) ) < cfg.sensitivity ) {
                $(ob).unbind("mousemove",track);
                // set hoverIntent state to true (so mouseOut can be called)
                ob.hoverIntent_s = 1;
                return cfg.over.apply(ob,[ev]);
            } else {
                // set previous coordinates for next time
                pX = cX; pY = cY;
                // use self-calling timeout, guarantees intervals are spaced out properly (avoids JavaScript timer bugs)
                ob.hoverIntent_t = setTimeout( function(){compare(ev, ob);} , cfg.interval );
            }
        };

        // A private function for delaying the mouseOut function
        var delay = function(ev,ob) {
            ob.hoverIntent_t = clearTimeout(ob.hoverIntent_t);
            ob.hoverIntent_s = 0;
            return cfg.out.apply(ob,[ev]);
        };

        // A private function for handling mouse 'hovering'
        var handleHover = function(e) {
            // next three lines copied from jQuery.hover, ignore children onMouseOver/onMouseOut
            var p = (e.type == "mouseover" ? e.fromElement : e.toElement) || e.relatedTarget;
            while ( p && p != this ) { try { p = p.parentNode; } catch(e) { p = this; } }
            if ( p == this ) { return false; }

            // copy objects to be passed into t (required for event object to be passed in IE)
            var ev = jQuery.extend({},e);
            var ob = this;

            // cancel hoverIntent timer if it exists
            if (ob.hoverIntent_t) { ob.hoverIntent_t = clearTimeout(ob.hoverIntent_t); }

            // else e.type == "onmouseover"
            if (e.type == "mouseover") {
                // set "previous" X and Y position based on initial entry point
                pX = ev.pageX; pY = ev.pageY;
                // update "current" X and Y position based on mousemove
                $(ob).bind("mousemove",track);
                // start polling interval (self-calling timeout) to compare mouse coordinates over time
                if (ob.hoverIntent_s != 1) { ob.hoverIntent_t = setTimeout( function(){compare(ev,ob);} , cfg.interval );}

            // else e.type == "onmouseout"
            } else {
                // unbind expensive mousemove event
                $(ob).unbind("mousemove",track);
                // if hoverIntent state is true, then call the mouseOut function after the specified delay
                if (ob.hoverIntent_s == 1) { ob.hoverIntent_t = setTimeout( function(){delay(ev,ob);} , cfg.timeout );}
            }
        };

        // bind the function to the two event listeners
        return this.mouseover(handleHover).mouseout(handleHover);
    };
})(jQuery);
</script>   <!-- Shortn.It version 1.7.4 -->
    <link rel="shorturl" href="http://www.promerica.com.do/a/RfWfM">
    <!-- End Shortn.It -->
<meta name="description" content="Las Tarjetas de Crédito de Banco Promerica están especialmente diseñadas para cubrir las necesidades particulares de un mercado exigente.  Gracias a...">
<style data-context="foundation-flickity-css">/*! Flickity v2.0.2
http://flickity.metafizzy.co
---------------------------------------------- */.flickity-enabled{position:relative}.flickity-enabled:focus{outline:0}.flickity-viewport{overflow:hidden;position:relative;height:100%}.flickity-slider{position:absolute;width:100%;height:100%}.flickity-enabled.is-draggable{-webkit-tap-highlight-color:transparent;tap-highlight-color:transparent;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.flickity-enabled.is-draggable .flickity-viewport{cursor:move;cursor:-webkit-grab;cursor:grab}.flickity-enabled.is-draggable .flickity-viewport.is-pointer-down{cursor:-webkit-grabbing;cursor:grabbing}.flickity-prev-next-button{position:absolute;top:50%;width:44px;height:44px;border:none;border-radius:50%;background:#fff;background:hsla(0,0%,100%,.75);cursor:pointer;-webkit-transform:translateY(-50%);transform:translateY(-50%)}.flickity-prev-next-button:hover{background:#fff}.flickity-prev-next-button:focus{outline:0;box-shadow:0 0 0 5px #09F}.flickity-prev-next-button:active{opacity:.6}.flickity-prev-next-button.previous{left:10px}.flickity-prev-next-button.next{right:10px}.flickity-rtl .flickity-prev-next-button.previous{left:auto;right:10px}.flickity-rtl .flickity-prev-next-button.next{right:auto;left:10px}.flickity-prev-next-button:disabled{opacity:.3;cursor:auto}.flickity-prev-next-button svg{position:absolute;left:20%;top:20%;width:60%;height:60%}.flickity-prev-next-button .arrow{fill:#333}.flickity-page-dots{position:absolute;width:100%;bottom:-25px;padding:0;margin:0;list-style:none;text-align:center;line-height:1}.flickity-rtl .flickity-page-dots{direction:rtl}.flickity-page-dots .dot{display:inline-block;width:10px;height:10px;margin:0 8px;background:#333;border-radius:50%;opacity:.25;cursor:pointer}.flickity-page-dots .dot.is-selected{opacity:1}</style><style data-context="foundation-slideout-css">.slideout-menu{position:fixed;left:0;top:0;bottom:0;right:auto;z-index:0;width:256px;overflow-y:auto;-webkit-overflow-scrolling:touch;display:none}.slideout-menu.pushit-right{left:auto;right:0}.slideout-panel{position:relative;z-index:1;will-change:transform}.slideout-open,.slideout-open .slideout-panel,.slideout-open body{overflow:hidden}.slideout-open .slideout-menu{display:block}.pushit{display:none}</style><!-- All in one Favicon 4.5 --><link rel="icon" href="http://www.promerica.com.do/wp-content/uploads/2014/07/Fav1.png" type="image/png">
<link rel="shortcut icon" href="http://www.promerica.com.do/wp-content/uploads/2014/07/Fav1.png">
<link rel="apple-touch-icon" href="http://www.promerica.com.do/wp-content/uploads/2014/07/Fav1.png">

<!-- WordPress Facebook Open Graph protocol plugin (WPFBOGP v2.0.13) http://rynoweb.com/wordpress-plugins/ -->
<meta property="fb:admins" content="https://www.facebook.com/promericard">
<meta property="og:url" content="http://www.promerica.com.do/?page_id=4002">
<meta property="og:title" content="Tarjetas Visa">
<meta property="og:site_name" content="Banco Promerica">
<meta property="og:description" content="Las Tarjetas de Crédito de Banco Promerica están especialmente diseñadas para cubrir las necesidades particulares de un mercado exigente.  Gracias a la fuerza tecnológica del Grupo Promerica, le podemos presentar nuestra amplia gama de tarjetas de crédito.  Estamos confiados que una de ellas está creada especialmente para usted. Ver contrato de adhesión.">
<meta property="og:type" content="website">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2014/08/Logo-Promerica-200.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Tarjeta-Platinum.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/10/Lama-Plazos-Visa.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2014/05/tarjeta-club-madre-y-bebe.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2014/07/Tarjeta-Club-Madre-y-Bebe.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2013/02/Crediplus-Visa.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Tarjeta-Promerica.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2015/09/Artista-Redes.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2015/09/infinite-Visa.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2016/01/Banner-OD-descripcion.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2016/05/Banner-mi-super-descripcion.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/05/Boton-Solicitud.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2017/02/Iberia-LandingPage.jpg">
<meta property="og:image" content="http://www.promerica.com.do/wp-content/uploads/2012/08/Tarjetas-Promerica.gif">
<meta property="og:locale" content="es_es">
<!-- // end wpfbogp -->
<style>.ios7.web-app-mode.has-fixed header{ background-color: rgba(255,255,255,.88);}</style>

<link href="./test_files/styles.css" rel="stylesheet" type="text/css">
<link href="./test_files/nav.css" rel="stylesheet" type="text/css">


<script language="javascript" src="./test_files/flashjs.js.download"></script><script type="text/javascript"><!--//--><![CDATA[//><!--

sfHover = function() {
    var sfEls = document.getElementById("nav").getElementsByTagName("LI");
    for (var i=0; i<sfEls.length; i++) {
        sfEls[i].onmouseover=function() {
            this.className+=" sfhover";
        }
        sfEls[i].onmouseout=function() {
            this.className=this.className.replace(new RegExp(" sfhover\\b"), "");
        }
    }
}
if (window.attachEvent) window.attachEvent("onload", sfHover);

//--><!]]></script></head>






<body id="tab0">
<div id="wrapper">
  <div id="header">
    <div id="brand"><a href="http://www.promerica.com.do/?page_id=21"><img src="./test_files/p.jpg" alt="Promerica" border="0" style="margin-left:25px; margin-top:5px;"></a></div>



<div>
    <table border="0" cellspacing="0" cellpadding="0">
    <tbody><tr>
<td>
   <div id="wpa_marquee"><a href="http://www.promerica.com.do/?p=1014"><h2><marquee>•  Dólar: Compra RD$47.00 | Venta RD$47.45...</marquee></h2></a></div></td>
    </tr>
    </tbody></table>
</div>


<div id="header-text" ;="" style="text-align: right" align="right">
<small>
<br>
<br>
<a title="Sitemap" href="http://www.promerica.com.do/?page_id=3728"> Tarifario</a>
<a>&nbsp;</a> <span>|</span><a>&nbsp;</a> 
<a title="Sitemap" href="http://www.promerica.com.do/?page_id=17"> Contáctenos </a>
<a>&nbsp;</a> <span>|</span><a>&nbsp;</a> 
<a title="Sitemap" href="http://www.promerica.com.do/?page_id=38"> Mapa del Sitio</a>
</small>
</div>


<div id="nav-wrapper">
      <ul id="nav">
    

<!--Menu Original:  <div class="nav"><ul id="menu-menu-header" class="menu"><li id="menu-item-4455" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4455"><a href="https://online.promerica.com.do">Promerica Online</a></li>
<li id="menu-item-3650" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-has-children menu-item-3650"><a href="http://www.promerica.com.do/">Inicio</a>
<ul class="sub-menu">
    <li id="menu-item-3609" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3609"><a href="#">Quienes Somos</a></li>
    <li id="menu-item-3616" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3616"><a href="http://www.promerica.com.do/?page_id=105">Historia</a></li>
    <li id="menu-item-3617" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3617"><a href="http://www.promerica.com.do/?page_id=135">Misión – Visión – Valores</a></li>
    <li id="menu-item-3620" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3620"><a href="http://www.promerica.com.do/?page_id=141">Mensaje Presidente del Consejo de Directores</a></li>
    <li id="menu-item-3619" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3619"><a href="http://www.promerica.com.do/?page_id=143">Mensaje del Presidente Ejecutivo</a></li>
    <li id="menu-item-4696" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4696"><a href="http://www.promerica.com.do/?page_id=4679">Calificación de Riesgo</a></li>
    <li id="menu-item-3618" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3618"><a href="http://www.promerica.com.do/?page_id=145">Memorias</a></li>
    <li id="menu-item-3637" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3637"><a href="http://www.promerica.com.do/?page_id=138">Estados Financieros</a></li>
    <li id="menu-item-3615" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3615"><a href="http://www.promerica.com.do/?page_id=42">Trabajar en Promerica</a></li>
</ul>
</li>
<li id="menu-item-3647" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-3647"><a href="#">Banca Personal</a>
<ul class="sub-menu">
    <li id="menu-item-3660" class="menu-item menu-item-type-post_type menu-item-object-page current-page-ancestor menu-item-3660"><a href="http://www.promerica.com.do/?page_id=151">Tarjetas de Crédito</a></li>
    <li id="menu-item-3659" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3659"><a href="http://www.promerica.com.do/?page_id=153">Préstamo Personal</a></li>
    <li id="menu-item-3677" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3677"><a href="http://www.promerica.com.do/?page_id=2717">Préstamos de Vehículos</a></li>
    <li id="menu-item-3658" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3658"><a href="http://www.promerica.com.do/?page_id=155">Certificados</a></li>
    <li id="menu-item-3662" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3662"><a href="http://www.promerica.com.do/?page_id=157">Cuentas de Ahorro</a></li>
    <li id="menu-item-3661" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3661"><a href="http://www.promerica.com.do/?page_id=159">CrediPlus</a></li>
    <li id="menu-item-3663" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3663"><a href="http://www.promerica.com.do/?page_id=161">Promerica Asiste</a></li>
    <li id="menu-item-3664" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-3664"><a href="http://www.promerica.com.do/?page_id=163">Banca Seguro</a>
    <ul class="sub-menu">
        <li id="menu-item-3868" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3868"><a href="http://www.promerica.com.do/?page_id=1651">Solicitud Seguro de Vida</a></li>
    </ul>
</li>
    <li id="menu-item-3645" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3645"><a href="http://www.promerica.com.do/wp-content/uploads/2014/07/Tarifario-2.pdf" onclick="__gaTracker('send', 'event', 'download', 'http://www.promerica.com.do/wp-content/uploads/2014/07/Tarifario-2.pdf');" target="_blank">Tarifario</a></li>
</ul>
</li>
<li id="menu-item-3648" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-3648"><a href="#">Banca Empresarial</a>
<ul class="sub-menu">
    <li id="menu-item-3669" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-3669"><a href="http://www.promerica.com.do/?page_id=769">Cuentas Bancarias</a>
    <ul class="sub-menu">
        <li id="menu-item-6288" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-6288"><a href="https://online.promerica.com.do/Galileo.PersonalBanking.UI.Web/PB/pages/administration/pbLoginPage.aspx">Promerica Online</a></li>
    </ul>
</li>
    <li id="menu-item-3672" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3672"><a href="http://www.promerica.com.do/?page_id=889">Cuenta Integra</a></li>
    <li id="menu-item-3670" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3670"><a href="http://www.promerica.com.do/?page_id=766">Préstamos Comerciales</a></li>
    <li id="menu-item-3668" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3668"><a href="http://www.promerica.com.do/?page_id=772">Inversiones</a></li>
    <li id="menu-item-3667" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3667"><a href="http://www.promerica.com.do/?page_id=774">Servicios Internacionales</a></li>
    <li id="menu-item-3666" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3666"><a href="http://www.promerica.com.do/?page_id=778">Nómina Electrónica</a></li>
</ul>
</li>
<li id="menu-item-3649" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-3649"><a href="#">Puntos de Atención</a>
<ul class="sub-menu">
    <li id="menu-item-3665" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3665"><a href="http://www.promerica.com.do/?page_id=756">Promerica Online</a></li>
    <li id="menu-item-3675" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3675"><a href="http://www.promerica.com.do/?page_id=1703">TeleAsistencia</a></li>
    <li id="menu-item-3651" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3651"><a href="http://www.promerica.com.do/?page_id=17">Centro de Contacto</a></li>
    <li id="menu-item-3673" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-3673"><a href="http://www.promerica.com.do/?page_id=992">Sucursales</a>
    <ul class="sub-menu">
        <li id="menu-item-4454" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4454"><a href="http://www.promerica.com.do/?page_id=4370">Sucursal más cercana</a></li>
    </ul>
</li>
    <li id="menu-item-3671" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3671"><a href="http://www.promerica.com.do/?page_id=759">Cajeros Automáticos</a></li>
    <li id="menu-item-3676" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3676"><a href="http://www.promerica.com.do/?page_id=1997">Redes Sociales</a></li>
</ul>
</li>
</ul></div>    -->

<!--Menu multinivel customizado en la sigueinte linea. Plugin "Multi-level Navigation"  -->


<!-- Multi-level Navigation Plugin v2.3.6 by Ryan Hellyer ... https://geek.hellyer.kiwi/multi-level-navigation/ -->
<div id="pixopoint_menu_wrapper1"><div id="pixopoint_menu1">        <ul class="sf-menu" id="suckerfishnav"><li><a href="http://www.promerica.com.do/">Inicio</a></li><li><a href="http://www.promerica.com.do/?page_id=4002#">Quienes somos</a>
  <ul>
    <li><a href="http://www.promerica.com.do/?page_id=105">Historia</a></li>
    <li><a href="http://www.promerica.com.do/?page_id=135">Misión Visión Valores</a></li>
    <li><a href="http://www.promerica.com.do/?page_id=141">Presidente del Consejo</a></li>
    <li><a href="http://www.promerica.com.do/?page_id=143">Presidente Ejecutivo</a></li>
    <li><a href="http://www.promerica.com.do/?page_id=5518">Relación Inversionistas</a></li>
    <li><a href="http://www.promerica.com.do/?page_id=42">Trabajar en Promerica</a></li>
  </ul>
</li>
<li class="current_page_parent current_page_item"><a href="http://www.promerica.com.do/?page_id=4002">Banca Personal</a><ul><li class="page_item page-item-153 page_item_has_children"><a href="http://www.promerica.com.do/?page_id=153">Préstamos</a>
<ul class="children">
    <li class="page_item page-item-4704"><a href="http://www.promerica.com.do/?page_id=4704">Préstamos Personales</a></li>
    <li class="page_item page-item-2717"><a href="http://www.promerica.com.do/?page_id=2717">Préstamos de Vehículos</a></li>
    <li class="page_item page-item-2789"><a href="http://www.promerica.com.do/?page_id=2789">Préstamos Hipotecarios</a></li>
</ul>
</li>
<li class="page_item page-item-151 page_item_has_children current_page_ancestor current_page_parent"><a href="http://www.promerica.com.do/?page_id=151">Tarjetas de Crédito</a>
<ul class="children">
    <li class="page_item page-item-4002 current_page_item"><a href="http://www.promerica.com.do/?page_id=4002">Tarjetas Visa</a></li>
    <li class="page_item page-item-3045"><a href="http://www.promerica.com.do/?page_id=3045">Tarjetas MasterCard</a></li>
    <li class="page_item page-item-159"><a href="http://www.promerica.com.do/?page_id=159">CrediPlus</a></li>
    <li class="page_item page-item-4749"><a href="http://www.promerica.com.do/?page_id=4749">Promerica Asiste</a></li>
</ul>
</li>
<li class="page_item page-item-4113"><a href="http://www.promerica.com.do/?page_id=4113">Cuenta Remunerada</a></li>
<li class="page_item page-item-157"><a href="http://www.promerica.com.do/?page_id=157">Cuentas de Ahorro</a></li>
<li class="page_item page-item-155"><a href="http://www.promerica.com.do/?page_id=155">Certificados</a></li>
<li class="page_item page-item-163"><a href="http://www.promerica.com.do/?page_id=163">Banca Seguro</a></li>
<li class="page_item page-item-5185"><a href="http://www.promerica.com.do/?page_id=5185">FATCA</a></li>
<li class="page_item page-item-6508"><a href="http://www.promerica.com.do/?page_id=6508">Promerica Móvil</a></li>
</ul></li>
<li><a href="http://www.promerica.com.do/?page_id=4002#">Banca Empresarial</a>
  <ul>
       <li><a href="http://www.promerica.com.do/?page_id=769">Cuentas Bancarias</a></li>
       <li><a href="http://www.promerica.com.do/?page_id=4122">Cuenta Remunerada</a></li>       
       <li><a href="http://www.promerica.com.do/?page_id=889">Cuenta Integra</a></li>
       <li><a href="http://www.promerica.com.do/?page_id=6208">Préstamos Empresariales</a></li>
       <li><a href="http://www.promerica.com.do/?page_id=772">Inversiones</a></li>
       <li><a href="http://www.promerica.com.do/?page_id=774/">Servicios Internacionales</a></li>
       <li><a href="http://www.promerica.com.do/?page_id=778">Nóminas Electrónicas</a></li>
       <li><a href="http://www.promerica.com.do/?page_id=5185">FATCA</a></li>
   </ul>
</li>
<li><a href="http://www.promerica.com.do/?page_id=4002#">Puntos de Atención</a>
  <ul>
      <li><a href="http://www.promerica.com.do/?page_id=756">Promerica Online</a></li>
      <li><a href="https://mobile.promerica.com.do/installer/">Promerica Móvil</a></li>
      <li><a href="http://www.promerica.com.do/?page_id=1703">TeleAsistencia</a></li>
      <li><a href="http://www.promerica.com.do/?page_id=17">Centro de contacto</a></li>
      <li><a href="http://www.promerica.com.do/?page_id=992">Sucursales</a></li>
      <li><a href="http://www.promerica.com.do/?page_id=759">Cajeros Automáticos</a></li>
      <li><a href="http://www.promerica.com.do/?page_id=3893">Puntos PagaTodo</a></li>
      <li><a href="http://www.promerica.com.do/?page_id=6213">Subagentes Promerica</a></li>
     </ul>
</li>
</ul>
    </div>
</div>

      </ul>
</div>

<div style="clear:both"></div>
</div>
  <div id="content-wrap">


<div id="sidebar">
<ul style="min-height:auto;">

    <li>            <div class="textwidget">&nbsp;
<div style="font-family:arial; text-transform:capitalize; font-size:16px; text-align: center; font-weight:bold; color:#006633">
Promerica Online

</div>

<div id="entrar-wrap">

<div id="entrar"><a href="https://online.promerica.com.do/" target="_blank">Ingresar</a></div>

</div></div>
        </li><li>           <div class="textwidget">&nbsp;
</div>
        </li><li>           <div class="textwidget"><center><a href="http://www.promerica.com.do/?page_id=4940" onclick="__gaTracker(&#39;send&#39;, &#39;event&#39;, &#39;outbound-widget&#39;, &#39;http://www.promerica.com.do/?page_id=4940&#39;, &#39;&#39;);" class="widget_sp_image-image-link" target="_self"><img class="aligncenter" style="max-width: 216px;" src="./test_files/Botones-2.png" alt="" border="0"></a></center>
<br></div>
        </li><li>           <div class="textwidget"><center><a href="http://www.promerica.com.do/?page_id=4933" onclick="__gaTracker(&#39;send&#39;, &#39;event&#39;, &#39;outbound-widget&#39;, &#39;http://www.promerica.com.do/?page_id=4933&#39;, &#39;&#39;);" class="widget_sp_image-image-link" target="_self"><img class="aligncenter" style="max-width: 216px;" src="./test_files/Botones-1.png" alt="" border="0"></a></center>
<br></div>
        </li><li>           <div class="textwidget"><center><a href="http://www.promerica.com.do/?p=4074" onclick="__gaTracker(&#39;send&#39;, &#39;event&#39;, &#39;outbound-widget&#39;, &#39;http://www.promerica.com.do/?p=4074&#39;, &#39;&#39;);" class="widget_sp_image-image-link" target="_self"><img class="aligncenter" style="max-width: 216px;" src="./test_files/Botones-3.png" alt="" border="0"></a></center>
<br>
</div>
        </li><li>           <div class="textwidget"><div style="font-family:arial; text-transform:capitalize; font-size:16px; text-align: center; font-weight:bold; color:#006633">
Buscador
</div></div>
        </li><li><form method="get" id="searchform" action="http://www.promerica.com.do/index.php">
<input type="text" name="s" id="s" value="">
<input type="submit" id="searchsubmit" value="Go">
</form></li><li>            <div class="textwidget">&nbsp;
</div>
        </li><li>           <div class="textwidget"><div style="font-family:arial; text-transform:capitalize; font-size:16px; text-align: center; font-weight:bold; color:#006633">
Novedades
</div></div>
        </li><li><h3></h3><div style="height: 48px;" class="vsrp_wrapper" data-delay-seconds="3" data-speed="2" data-direction="0"><div class="vsrp_div" style="height: 16px;"><a href="http://www.promerica.com.do/?p=6328">• Líneas Verdes</a></div><div class="vsrp_div" style="height: 16px;"><a href="http://www.promerica.com.do/?p=5719">• Mi Super</a></div></div></li> </ul>
 </div>
 
<div id="content-body">
<meta property="twitter:account_id" content="4503599627408699">

<div class="breadcrumb"><a href="http://www.promerica.com.do/">Banco Promerica</a>  » <a href="http://www.promerica.com.do/?page_id=38">Sitemap</a> » <a href="http://www.promerica.com.do/?page_id=30">Banca Personal</a> » <a href="http://www.promerica.com.do/?page_id=151">Tarjetas de Crédito</a> » Tarjetas Visa</div>
<!-- Facebook Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','//connect.facebook.net/en_US/fbevents.js');

fbq('init', '963946873665988');
fbq('track', "PageView");</script>
<noscript><img height="1" width="1" style="display:none" src="./test_files/tr"></noscript>
<!-- End Facebook Pixel Code -->

            <div class="post" id="post-4002">
        
            <div class="entrytext">
                <p>
    &nbsp;
</p>
<h2 align="justify" style="text-align: left;">
    <span style="color: #006233;">Tarjetas de Crédito Visa</span><br>
</h2>
<p>
    &nbsp;
</p>
<p align="justify" style="text-align: right;">
    <a href="http://www.promerica.com.do/?page_id=533" target="_self" title="Puntos Promerica">Ver Programa de Puntos Promerica</a>
</p>
<p align="justify" style="text-align: right;">
    <a href="http://www.promerica.com.do/wp-content/uploads/2016/08/REGLAMENTO-GENERAL-PROGRAMA-DE-LEALTAD-PUNTOS-PROMERICA.pdf" target="_blank">Reglamento General Programa de Lealtad</a>
</p>
<p align="justify" style="text-align: right;">
    <a href="http://www.promerica.com.do/?page_id=732" target="_self"><span style="color: #006233;"><span style="color: #006233;">¿Que debe saber sobre su tarjeta?</span>&nbsp;</span></a>
</p>
<p align="justify" style="text-align: right;">
    <a href="http://www.promerica.com.do/wp-content/uploads/2014/07/Telefonos-Visa-Internacional.pdf" target="_blank">Servicio Visa Internacional</a>
</p>
<p align="justify" style="text-align: right;">
    <a href="http://www.promerica.com.do/wp-content/uploads/2015/03/Contrato-Tarjeta-de-Credito.pdf" target="_blank">Contrato de Adhesión&nbsp;Tarjeta de Crédito</a>
</p>
<p align="justify" style="text-align: center;">
    <img alt="" class="aligncenter  wp-image-2019" src="./test_files/Tarjetas-Promerica.gif" title="Tarjetas-Promerica">
</p>
<p align="justify">
    Las Tarjetas de Crédito de Banco Promerica están especialmente diseñadas para cubrir las necesidades particulares de un mercado exigente.&nbsp; Gracias a la fuerza tecnológica del Grupo Promerica, le podemos presentar nuestra amplia gama de tarjetas de crédito.&nbsp; Estamos confiados que una de ellas está creada especialmente para usted.
</p>
<p align="justify">
    &nbsp;
</p>
<h2 class="collapseomatic  find-me" id="id9576" rel="tarjetas-highlander" tabindex="" title="Iberia Promerica" data-findme="400">Iberia Promerica</h2><h2 id="swap-id9576" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id9576" class="collapseomatic_content ">
<p>
    &nbsp;
</p>
<p>
    <img alt="" class="aligncenter size-full wp-image-6353" height="235" src="./test_files/Iberia-LandingPage.jpg" width="710" srcset="http://www.promerica.com.do/wp-content/uploads/2017/02/Iberia-LandingPage.jpg 710w, http://www.promerica.com.do/wp-content/uploads/2017/02/Iberia-LandingPage-300x99.jpg 300w" sizes="(max-width: 710px) 100vw, 710px">
</p>
<p>
    &nbsp;
</p>
<p>
    Viajar en Iberia es &nbsp;cómodo con los privilegios que ofrece la nueva tarjeta <strong>Iberia Promerica</strong>
</p>
<p>
    Con esta tarjeta recibes Avios con tus consumos, los cuales podrás utilizar en el próximo destino de viaje a través de Iberia.
</p>
<p>
    &nbsp;
</p>
<p>
    Con esta tarjeta recibes Avios de bienvenida*:
</p>
<p>
    – Iberia Promerica Infinite: te otorga 15,000 Avios de bienvenida
</p>
<p>
    – Iberia Promerica Platinum te otorga 10,000 Avios de bienvenida.
</p>
<p>
    &nbsp;
</p>
<p>
    Con todos tus demás consumos, dentro y fuera del país, recibes 1 Avios por cada dólar o su equivalente en moneda nacional.
</p>
<p>
    &nbsp;
</p>
<p>
    Además, recibirás los beneficios Visa de:
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Servicios&nbsp; de&nbsp; emergencia&nbsp; médica&nbsp; Internacional&nbsp; más Certificado Schengen:</strong>
</p>
<p>
    – Tus servicios de emergencia médica internacional cubren caso de accidente o emergencia que ocurran muestras disfrutas de tus viajes en el exterior. Estos servicios incluyen&nbsp; gastos médicos, gastos dentales, gastos de receta médica, transporte y alojamiento como se definen el los términos y condiciones
</p>
<p>
    &nbsp;
</p>
<p>
    – El tarjetahabiente puede obtener un certificado Schengen sin cargo adicional, el programa IEMS&nbsp; (Servicios&nbsp; Médico de&nbsp; emergencia Internacional) cumple con todos los requerimiento.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Seguro de Accidente de Viaje:</strong>
</p>
<p>
    – Al pagar la totalidad de tus boletos con tu tarjeta&nbsp; Visa Platinum recibes gratuitamente&nbsp; y a&nbsp; nivel mundial incluyendo tu país de domicilio una protección contra muerte&nbsp; accidental o desmembramiento cuando te encuentres disfrutando en el destino de tu viaje.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Pérdida y Demora de Equipaje (beneficio exclusivo para tarjetahabientes Iberia Promerica Infinite): &nbsp;</strong>
</p>
<p>
    – Recibes gratuitamente y a nivel mundial, una protección contra&nbsp; pérdida de equipaje&nbsp; que ocurra cuando tus molestas estén&nbsp; bajo la responsabilidad de un medio de transporte registrado. Asimismo cuentas&nbsp; con seguro en demora de equipaje. Esta protección comienza&nbsp; desde la cuarta hora de demora y te compensara por cada hora de demora hasta el monto&nbsp; indicado en los términos y condiciones
</p>
<p>
    &nbsp;
</p>
<p>
    *La tarjeta <strong>Iberia Promerica Infinite</strong> te otorga 15,000 AVIOS de bienvenida al activar tu tarjeta titular y consumir un monto mínimo de US$1,500 o su equivalente en moneda nacional, en los primeros tres meses de activada la tarjeta.
</p>
<p>
    &nbsp;
</p>
<p>
    *La tarjeta <strong>Iberia Promerica Platinum</strong> otorga 10,000 AVIOS de bienvenida al activar tu tarjeta titular y consumir un monto mínimo de US$1,000 o su equivalente en moneda nacional, en los primeros tres meses de activada la tarjeta.
</p>
<p style="text-align: center;">
    &nbsp;&nbsp; &nbsp;<a href="http://www.promerica.com.do/?page_id=1061" title="Solicitud de Tarjeta de Crédito"><img alt="" class="aligncenter size-full wp-image-381" height="38" src="./test_files/Boton-Solicitud.jpg" title="Boton Solicitud" width="154"></a>
</p>
<p>
    &nbsp;
</p>
<p>
    <span style="line-height: 20.8px;"></span></p></div>
<p></p>
<p>
    <span style="line-height: 20.8px; text-align: justify;"></span></p><h2 class="collapseomatic highlight find-me" id="id9267" rel="tarjetas-highlander" tabindex="" title="Mi Super" data-findme="710">Mi Super</h2><h2 id="swap-id9267" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id9267" class="collapseomatic_content ">
<p></p>
<p>
    &nbsp;
</p>
<h2>
    <span style="color: #006233;">Mi Super</span><br>
</h2>
<p>
    &nbsp;
</p>
<p style="text-align: center;">
    <img alt="" class="size-full wp-image-5714 aligncenter" height="265" src="./test_files/Banner-mi-super-descripcion.jpg" style="" title="" width="710" srcset="http://www.promerica.com.do/wp-content/uploads/2016/05/Banner-mi-super-descripcion.jpg 710w, http://www.promerica.com.do/wp-content/uploads/2016/05/Banner-mi-super-descripcion-300x111.jpg 300w" sizes="(max-width: 710px) 100vw, 710px">&nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Mi Super es la única tarjeta en el mercado que te ofrece más beneficios al realizar tus compras en <strong>los supermercados del país</strong>;&nbsp; a través de su atractivo plan de&nbsp; acumulación de Puntos Promerica, nuestro programa de lealtad que se ajusta a todas tus necesidades.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Beneficios principales:</strong>
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    ► 3% de acumulación en tus compras en todos los supermercados a nivel nacional.
</p>
<p style="margin-left: 40px;">
    ► 2% de acumulación en tus compras online realizadas en US$.
</p>
<p style="margin-left: 40px;">
    ► 0.5% en los demás consumos tanto en RD$ como en US$.
</p>
<p style="margin-left: 40px;">
    ► Cada punto equivale a RD$1 que podrás canjear por crédito a cuenta, boletos aéreos, hoteles nacionales e internaciones, certificados de compra y eventos de temporada.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Otros beneficios:</strong>
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    ► Crediplus, programa de crédito diferido que te permite pagar en cuotas las compras realizadas en comercios afiliados, hasta &nbsp;14 meses sin intereses y hasta 36 meses con intereses.
</p>
<p style="margin-left: 40px;">
    ► Promerica Asiste, programa de asistencia vial y domiciliaria.
</p>
<p style="margin-left: 40px;">
    ► Seguro de Accidentes de Viaje en Medios de Transporte hasta US$ 250,000.
</p>
<p style="margin-left: 40px;">
    ► Seguro para Autos Alquilados.
</p>
<p style="margin-left: 40px;">
    ► Servicio de reemplazo de emergencia de la tarjeta en caso de pérdida o robo.
</p>
<p style="margin-left: 40px;">
    ► Centro de Información para viajes.
</p>
<p style="margin-left: 40px;">
    ► Centro de Asistencia al cliente Visa.
</p>
<p style="margin-left: 40px;">
    ► Acceso a Promerica Online 24/7.
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Requisitos:</strong>
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    ► Poseer cédula de identidad.
</p>
<p style="margin-left: 40px;">
    ► Ser residente dominicano.
</p>
<p style="margin-left: 40px;">
    ► Edad comprendida entre 21 y 65 años.
</p>
<p style="margin-left: 40px;">
    ► Poseer referencias bancarias.
</p>
<p style="margin-left: 40px;">
    ► Ingresos mínimos según indicados.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Cuenta con el Centro de Interacción con el Cliente (CIC), a través del cual recibirá atención personalizada, atendiendo sus consultas, reclamos, solicitudes y asesoramiento, con solo llamar al teléfono 809 732-6006 o 1-809-200-0258 desde el Interior.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: center;">
    <a href="http://www.promerica.com.do/?page_id=1061" title="Solicitud de Tarjeta de Crédito"><img alt="" class="aligncenter size-full wp-image-381" height="38" src="./test_files/Boton-Solicitud.jpg" title="Boton Solicitud" width="154"></a>
</p>
<p>
    </p></div>
<p></p>
<p>
    <span style="line-height: 20.8px; text-align: justify;"></span></p><h2 class="collapseomatic highlight find-me" id="id8153" rel="tarjetas-highlander" tabindex="" title="Office Depot" data-findme="730">Office Depot</h2><h2 id="swap-id8153" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id8153" class="collapseomatic_content ">
<p></p>
<p>
    <a id="Office Depot" name="Office Depot"><span style="line-height: 20.8px; text-align: justify;">.</span></a>
</p>
<p style="text-align: center;">
    <img alt="" class="size-full wp-image-5115 aligncenter" height="290" src="./test_files/Banner-OD-descripcion.jpg" style="" title="" width="710">
</p>
<p>
    &nbsp;
</p>
<p>
    Es una tarjeta que te brinda la facilidad de adquirir lo último en tecnología, oficina y entretenimiento,&nbsp;además de obtener beneficios especiales.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Beneficios</strong>
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp; &nbsp;► 6% Puntos Promerica en las compras realizadas en las tiendas Office Depot.<br>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp; &nbsp;►&nbsp;2% de Puntos Promerica en tus compras hechas con tu Tarjeta Office Depot Promerica en centros educativos (colegios, universidades, institutos, etc.).<br>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp; &nbsp;►&nbsp;1% de Puntos Promerica otros comercios, tanto dentro como fuera del país.<br>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp; &nbsp;►&nbsp;20% de descuento en los centros de fotocopiado de Office Depot.<br>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp; &nbsp;►&nbsp;CrediPlus, plan de financiamiento que le permite pagar a plazos sus compras realizadas en comercios afiliados desde 14 meses sin intereses hasta 36 meses con intereses.<br>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp; &nbsp;►&nbsp;Seguros de viajes:
</p>
<p style="margin-left: 40px;">
    &nbsp;
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>&gt;&gt;</strong> Seguro de Accidentes en Viaje.
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>&gt;&gt;</strong> Seguro para Autos Alquilados.
</p>
<p>
    <br>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;►&nbsp;Seguros opcionales:
</p>
<p style="margin-left: 40px;">
    &nbsp;
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>&gt;&gt;</strong> Promerica Asiste.
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>&gt;&gt;</strong> Cuota Protegida Promerica.
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>&gt;&gt;</strong> Programa Viajero.
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp; &nbsp;► Acceso a Promerica Online 24/7.
</p>
<p style="margin-left: 40px;">
    &nbsp;
</p>
<p style="margin-left: 40px;">
    &nbsp;
</p>
<p>
    <strong>Requisitos:</strong>
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;► Ser residente dominicano.
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;► Edad comprendida entre 21 y 65 años.
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;►&nbsp;Poseer referencias bancarias.
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;► Ingresos mínimos RD$15,000.00
</p>
<p>
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: center;">
    <a href="http://www.promerica.com.do/?page_id=1061" title="Solicitud de Tarjeta de Crédito"><img alt="" class="size-full wp-image-381 aligncenter" height="38" src="./test_files/Boton-Solicitud.jpg" title="Boton Solicitud" width="154"></a>
</p>
<p>
    &nbsp;
</p>
<p>
    <span style="line-height: 20.8px;"></span></p></div>
<p></p>
<p>
    <span style="line-height: 20.8px; text-align: justify;"></span></p><h2 class="collapseomatic highlight find-me" id="id3854" rel="tarjetas-highlander" tabindex="" title="Visa Infinite" data-findme="710">Visa Infinite</h2><h2 id="swap-id3854" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id3854" class="collapseomatic_content ">
<p></p>
<p>
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: center;">
    <img alt="" class="size-full wp-image-5115 aligncenter" height="290" src="./test_files/infinite-Visa.jpg" style="" title="" width="710" srcset="http://www.promerica.com.do/wp-content/uploads/2015/09/infinite-Visa.jpg 710w, http://www.promerica.com.do/wp-content/uploads/2015/09/infinite-Visa-300x122.jpg 300w" sizes="(max-width: 710px) 100vw, 710px">
</p>
<p>
    Con un diseño innovador y exclusivo, inspirada en una obra de arte por el artista dominicano José Perdomo, la nueva tarjeta VISA Infinite cuenta con tecnología de chip para brindarle mayor seguridad en sus compras. Impresa bajo el formato “Quick Read”, una propuesta única en el país implementada para darle mayor facilidad al leer la información de su tarjeta.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Beneficios</strong>
</p>
<p>
    Con la nueva tarjeta de crédito Visa Infinite, usted forma parte de un exclusivo mundo de beneficios y privilegios que le permiten gozar de los mejores servicios, mayor protección en sus viajes y un estilo de vida sin igual:
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    ► Programa de Acumulación Acelerada de Puntos, el cual le permite acumular Puntos Promerica por cada RD$100.00 de compra o su equivalente en dólares, dentro y fuera de República Dominicana:
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 80px;">
    <strong>&gt;&gt;</strong> 3 Puntos Promerica por compras en el extranjero.
</p>
<p style="margin-left: 80px;">
    <strong>&gt;&gt;</strong>&nbsp;2 Puntos Promerica por compras en aerolíneas, aeropuertos, agencias de viaje, hoteles, alquiler de autos y restaurantes.
</p>
<p style="margin-left: 80px;">
    <strong>&gt;&gt;</strong> 1 Punto Promerica por compras en otros comercios.
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    ► 2 entradas gratis a cualquier museo del mundo (es necesario reportar su compra).
</p>
<p style="margin-left: 40px;">
    ► Membresía anual Priority Pass totalmente gratis, con accesos incluidos a las salas VIP participantes alrededor del mundo.
</p>
<p style="margin-left: 40px;">
    ► 4,500 Puntos Promerica de bienvenida.
</p>
<p style="margin-left: 40px;">
    ► Crediplus, plan de financiamiento que le permite pagar a plazos sus compras realizadas en comercios afiliados:
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 80px;">
    <strong>&gt;&gt;</strong> Hasta 14 meses sin intereses.
</p>
<p style="margin-left: 80px;">
    <strong>&gt;&gt;</strong> Hasta 36 meses con intereses.
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    ► Tasa de interés anual de 42% en pesos y 36% en dólares.
</p>
<p style="margin-left: 40px;">
    ► Seguridad Vial.
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Beneficios al Viajar </strong>
</p>
<p>
    &nbsp;
</p>
<p style="margin-left: 40px;">
    ► Seguro de Accidentes de Viaje en Medios de Transporte hasta US$1,500,000.00
</p>
<p style="margin-left: 40px;">
    ► Seguro de Accidentes de Destino de Viajes por US$50,000.00
</p>
<p style="margin-left: 40px;">
    ► Seguro de Alquiler de Autos hasta US$50,000.00
</p>
<p style="margin-left: 40px;">
    ►&nbsp;Seguro de Demora de Equipaje hasta US$500.00
</p>
<p style="margin-left: 40px;">
    ► Seguro de Pérdida de Equipaje hasta US$1,500.00
</p>
<p style="margin-left: 40px;">
    ► Seguro de Garantía Extendida hasta&nbsp; US$25,000.00
</p>
<p style="margin-left: 40px;">
    ► Seguro de Protección de Precios y Compras hasta US$1,000.00
</p>
<p style="margin-left: 40px;">
    ► Seguro de Cancelación de Viajes hasta US$2,500.00
</p>
<p style="margin-left: 40px;">
    ► Seguro de Demora de Vuelos hasta&nbsp; US$200.00
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    <strong style="font-family: arial, sans-serif; line-height: 18px;">Conoce un poco más del artista José Perdomo:</strong>
</p>
<p style="text-align: justify;">
    <a href="./test_files/Artista-Redes.jpg" rel="" style="" target="" title=""><img alt="Reseña Artista José Perdomo" class="size-full wp-image-5126 aligncenter" height="316" src="./test_files/Artista-Redes.jpg" style="" title="" width="694" srcset="http://www.promerica.com.do/wp-content/uploads/2015/09/Artista-Redes.jpg 2754w, http://www.promerica.com.do/wp-content/uploads/2015/09/Artista-Redes-300x136.jpg 300w, http://www.promerica.com.do/wp-content/uploads/2015/09/Artista-Redes-1024x467.jpg 1024w, http://www.promerica.com.do/wp-content/uploads/2015/09/Artista-Redes-900x410.jpg 900w" sizes="(max-width: 694px) 100vw, 694px"></a>
</p>
<p>
    &nbsp;
</p>
<p>
    <span style="line-height: 20.8px;"></span></p></div>
<p></p>
<p align="justify">
    </p><h2 class="collapseomatic  find-me" id="id2016" rel="tarjetas-highlander" tabindex="" title="Promerica" data-findme="540">Promerica</h2><h2 id="swap-id2016" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id2016" class="collapseomatic_content ">
<p></p>
<h2>
    <span style="color: #006233;">Promerica</span><br>
</h2>
<p>
    &nbsp; <img alt="" class="alignleft wp-image-364" height="105" src="./test_files/Tarjeta-Promerica.jpg" style="margin-right: 5px; margin-left: 5px;" title="Tarjeta Promerica" width="160">
</p>
<p style="text-align: justify;">
    Un producto revolucionario e innovador, la Tarjeta de Crédito Promerica está especialmente diseñada para cubrir las necesidades particulares de un exigente mercado, tomando como punto de partida un producto masivo y convirtiéndolo en uno hecho a la medida.Con ella, y gracias a los avances tecnológicos del Grupo Promerica, tiene la oportunidad de personalizar donde y cuando recibirá mayores beneficios.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Como tarjetahabientes de Visa Promerica cuenta, además, con una Oferta Inicial de Consolidación de Deudas, con la que puede obtener un ahorro sustancial en los intereses pagados, al transferir sus deudas desde otras instituciones financieras.Características y BeneficiosPrograma de Puntos Promerica, un innovador y exclusivo programa, el cual acumula en puntos el 1% de sus compras y cuenta con dos planes adicionales de acumulacion:
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    1. Usted gana el DOBLE de puntos en el establecimiento de su preferencia.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    2. Usted gana el DOBLE de puntos en una de cinco categorías de establecimientos donde usted realiza la mayor cantidad de sus consumos.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Revisión automática de su límite de crédito al momento de la renovación.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Oferta inicial de consolidación de deudas, con la que puede transferir sus deudas desde otras instituciones financieras y pagar en cómodas cuotas, al más bajo interés.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    CREDIPLUS, sistema que le ofrece una línea de crédito adicional, con atractivas tasas y cómodas cuotas de 6 a 36 meses cargadas mensualmente a su tarjeta. Además puede realizar compras a 6 MESES SIN INTERESES en algunos de los más de 70 establecimientos afiliados.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Promerica Asiste, un programa exclusivo que te asegura asistencia vial, domiciliaria y de viajes con cobertura oportuna e inmediata.
</p>
<p style="text-align: justify;">
    – Libre de cargos por costo de emisión.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Protección contra pérdida y robo de las tarjetas.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Hasta 24 meses de financiamiento.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Cuenta con el Centro de Interacción con el Cliente (CIC), a través del cual recibirá atención personalizada, atendiendo sus consultas, reclamos, solicitudes y asesoramiento con solo llamar al teléfono 809 732-6006 o 1-809-200-0258 desde el Interior.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: center;">
    <a href="http://www.promerica.com.do/?page_id=1061" title="Solicitud de Tarjeta de Crédito"><img alt="" class="aligncenter  wp-image-381" src="./test_files/Boton-Solicitud.jpg" title="Boton Solicitud"></a>
</p>
<p>
    &nbsp;
</p>
<p>
    </p></div>
<p></p>
<p align="justify">
    </p><h2 class="collapseomatic highlight find-me" id="id9705" rel="tarjetas-highlander" tabindex="" title="Crediplus Visa" data-findme="440">Crediplus Visa</h2><h2 id="swap-id9705" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id9705" class="collapseomatic_content ">
<p></p>
<p align="justify">
    &nbsp;
</p>
<h2>
    <span style="color: #006233;">Crediplus Visa</span><br>
</h2>
<p>
    &nbsp;
</p>
<p align="justify">
    <img alt="" class="wp-image-2922 alignleft" height="94" src="./test_files/Crediplus-Visa.jpg" title="Crediplus-Visa" width="159">
</p>
<p>
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
</p>
<p style="text-align: justify;">
    Crediplus Visa es una Tarjeta de Crédito que le permite con un solo plástico, realizar consumos revolventes en pesos y dólares, además de financiar sus compras extraordinarias en cómodas cuotas mensuales.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    <strong>Beneficios:</strong>
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p>
    – Línea Crédito con disponibilidad en RD$ y USD.
</p>
<p>
    &nbsp;
</p>
<p>
    – Línea de crédito adicional para compras en cuotas.
</p>
<p>
    &nbsp;
</p>
<p>
    – Planes de financiamientos de 6 y 12 meses sin intereses.
</p>
<p>
    &nbsp;
</p>
<p>
    – Libertad de diferir el pago total o parcial de su corte.
</p>
<p>
    &nbsp;
</p>
<p>
    – Atractivo plan de lealtad donde acumulas el doble de puntos al seleccionar el establecimiento o categoría de preferencia.
</p>
<p>
    &nbsp;
</p>
<p>
    – Promerica Asiste, servicio opcional que ofrece asistencia vial, domiciliaria y de viajes.
</p>
<p>
    &nbsp;
</p>
<p>
    – Retiro de Efectivo.
</p>
<p>
    &nbsp;
</p>
<p>
    – Emisión libre de costo.
</p>
<p>
    &nbsp;
</p>
<p>
    – Protección contra pérdida y robo.
</p>
<p>
    &nbsp;
</p>
<p>
    – Aprobación Inmediata. &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    <strong>Requisitos:</strong>
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Ser residente dominicano.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Edad comprendida entre 21 y 65 años.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Poseer referencias bancarias.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Ingresos mínimos RD$15,000.00
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Aprobación y entrega inmediata en nuestros Puntos de Negocios ubicados en las tiendas: Plaza Lama,&nbsp;Ikea y Jumbo.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Cuenta con el Centro de Interacción con el Cliente (CIC), a través del cual recibirá atención personalizada, atendiendo sus consultas, reclamos, solicitudes y asesoramiento, con solo llamar al teléfono 809 732-6006 o 1-809-200-0258 desde el Interior.
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp;
</p>
<p style="text-align: center;">
    <a href="http://www.promerica.com.do/?page_id=1061"><img alt="" class="aligncenter" height="38" src="./test_files/Boton-Solicitud.jpg" title="Boton Solicitud" width="154"></a>
</p>
<p>
    </p></div>
<p></p>
<p align="justify">
    </p><h2 class="collapseomatic  find-me" id="id6131" rel="tarjetas-highlander" tabindex="" title="Club Madre y Bebe" data-findme="560">Club Madre y Bebe</h2><h2 id="swap-id6131" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id6131" class="collapseomatic_content ">
<p></p>
<h2>
    <span style="color: #006233;">Club Madre y Bebe</span><br>
</h2>
<p>
    &nbsp;
</p>
<p style="text-align: left;">
    &nbsp;<img alt="" class="alignnone wp-image-3848 size-full" height="98" src="./test_files/Tarjeta-Club-Madre-y-Bebe.jpg" width="150">
</p>
<p align="justify">
    <img alt="" class="wp-image-2922 alignleft" height="0" src="./test_files/Tarjeta-Club-Madre-y-Bebe(1).jpg" title="Club Madre y Bebe" width="0">
</p>
<p>
    &nbsp; La Tarjeta Visa Club Madre y Bebé ha sido diseñada para ser la aliada de las madres dominicanas en una etapa tan importante de su vida, como lo es la maternidad y crianza de los hijos.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Beneficios:</strong>
</p>
<p>
    &nbsp;
</p>
<p>
    – Membresía a Club Madre y Bebé. – Programa de&nbsp;<a href="http://www.clubmadreybebe.com/descuentos" target="_blank" title="Programa de Descuentos Visa Promerica Club Madre y Bebe">descuentos</a>&nbsp;y promociones especiales.
</p>
<p>
    &nbsp;
</p>
<p>
    – Participación en actividades y eventos.
</p>
<p>
    &nbsp;
</p>
<p>
    – Programa de Lealtad Puntos Promerica, el cual te ofrece diferentes opciones de canje: Viajes y Vacaciones, Certificado de Regalo, Entradas a Eventos y Conciertos, Crédito a Cuenta y Canjes Directos en Establecimientos Afiliados a Visanet. &nbsp; Además,&nbsp; acumulas el doble de puntos según el plan de tu elección:
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>– Plan Personalizado:</strong>&nbsp;&nbsp; Seleccionando la categoría preferida: Hogar, Entretenimiento, Viajes, Cuidado Personal o Salud.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>– Plan Focalizado:</strong>&nbsp;Eligiendo el establecimiento de tu preferencia. – Promerica Asiste,&nbsp; que te ofrece asistencia vial, domiciliaria y de viajes.
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Esta tarjeta apoya iniciativas solidarias dirigidas a madres y niños de nuestro país a través de organizaciones sin fines de lucro, al utilizarla, sumas tu voluntad a una noble causa.</strong>
</p>
<p>
    &nbsp;
</p>
<p>
    <strong>Requisitos:</strong>
</p>
<p>
    &nbsp;
</p>
<p>
    – Ser residente dominicano.
</p>
<p>
    &nbsp;
</p>
<p>
    – Edad comprendida entre 21 y 65 años.
</p>
<p>
    &nbsp;
</p>
<p>
    – Poseer referencias bancarias.
</p>
<p>
    &nbsp;
</p>
<p>
    – Ingresos mínimos RD$15,000.00
</p>
<p>
    &nbsp;
</p>
<p>
    Cuenta con el Centro de Interacción con el Cliente (CIC), a través del cual recibirá atención personalizada, atendiendo sus consultas, reclamos, solicitudes y asesoramiento con solo llamar al teléfono 809.732.6006 o 1.809.200-.258 desde el Interior. &nbsp;
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp;
</p>
<p>
    <a href="http://www.promerica.com.do/?page_id=3372"><img alt="" class="aligncenter wp-image-381 size-full" height="38" src="./test_files/Boton-Solicitud.jpg" title="Clic aquí" width="154"></a>
</p>
<div>
    &nbsp;
</div>
<p>
    </p></div>
<p></p>
<p align="justify">
    </p><h2 class="collapseomatic  find-me" id="id9977" rel="tarjetas-highlander" tabindex="" title="Lama Plazos" data-findme="600">Lama Plazos</h2><h2 id="swap-id9977" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id9977" class="collapseomatic_content ">
<p></p>
<h2>
    <span style="color: #006233;">Lama Plazos</span><br>
</h2>
<p style="text-align: center;">
    <img alt="" class="size-full wp-image-2400 alignleft" height="102" src="./test_files/Lama-Plazos-Visa.jpg" style="" title="" width="169">
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Ahora con mucho más beneficios!!!!
</p>
<p>
    <strong>Doble línea de crédito:</strong>
</p>
<p>
    <span style="text-decoration: underline;">Línea Visa</span>
</p>
<p>
    – 6% de ahorro en todas las compras en Plaza Lama.
</p>
<p>
    – Acumulación de Puntos Promerica para tus otras compras.
</p>
<p>
    – Ideal para usarla dentro y fuera del país.
</p>
<p>
    &nbsp;
</p>
<p>
    <span style="text-decoration: underline;">Línea Plaza Lama</span>
</p>
<p>
    – Hasta 3 veces* tu límite asignado para compras en las tiendas Plaza Lama con los mejores planes. * Algunas condiciones aplican. &nbsp;
</p>
<p>
    &nbsp;
</p>
<p style="text-align: justify;">
    <strong>Beneficios:</strong>
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p>
    – Aprobación y entrega inmediata en Plaza Lama.
</p>
<p>
    &nbsp;
</p>
<p>
    – Planes hasta 14 meses sin intereses para esas compras extraordinarias.
</p>
<p>
    &nbsp;
</p>
<p>
    – Descuentos de temporada.
</p>
<p>
    &nbsp;
</p>
<p>
    – Rifas y concursos periódicos por compras en las tiendas Plaza Lama.
</p>
<p>
    &nbsp;
</p>
<p>
    – Disponibilidad de retiros en efectivo en todos los cajeros de la red ATH y PLUS.
</p>
<p>
    &nbsp;
</p>
<p>
    – Seguro de accidentes de viajes.
</p>
<p>
    &nbsp;
</p>
<p>
    – Seguro de alquiler de vehículos.
</p>
<p>
    &nbsp;
</p>
<p>
    – Moderno proceso de autorización y desembolso para compras a plazos.
</p>
<p>
    &nbsp;
</p>
<p>
    Cuenta con el Centro de Interacción con el Cliente (CIC), a través del cual recibirá atención personalizada, atendiendo sus consultas, reclamos, solicitudes y asesoramiento con solo llamar al teléfono 809 732-6006 o 1-809-200-0258 desde el Interior. &nbsp;
</p>
<p>
    &nbsp;
</p>
<p style="text-align: center; padding-left: 30px;">
    <a href="http://www.promerica.com.do/?page_id=1061" title="Solicitud de Tarjeta de Crédito"><img alt="" class="aligncenter  wp-image-381" height="38" src="./test_files/Boton-Solicitud.jpg" title="Boton Solicitud" width="154"></a>
</p>
<p>
    &nbsp;
</p>
<p>
    </p></div>
<p></p>
<p align="justify">
    </p><h2 class="collapseomatic  find-me" id="id678" rel="tarjetas-highlander" tabindex="" title="Platinum" data-findme="650">Platinum</h2><h2 id="swap-id678" alt="" class="colomat-swap" style="display:none;">Cerrar</h2><div id="target-id678" class="collapseomatic_content ">
<p></p>
<h2>
    <span style="color: #006233;">Platinum</span><br>
</h2>
<p>
    &nbsp; <img alt="" class="alignleft wp-image-393" height="106" src="./test_files/Tarjeta-Platinum.jpg" style="margin-right: 5px; margin-left: 5px;" title="Tarjeta Platinum" width="159">En Promerica sabemos que existen personas que conocen el verdadero significado del prestigio, distinción y exclusividad. &nbsp;
</p>
<p>
    &nbsp;
</p>
<p style="text-align: justify;">
    Al pertenecer a nuestro muy selecto grupo de clientes preferenciales, usted disfrutará de los más altos niveles de servicios, aceptación y exclusividad, que hacen de su Promerica Platinum una poderosa herramienta de compras y facilidad crediticia.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Promerica Platinum dispone para usted una serie de programas de atención y seguridad, tanto personal como de su cuenta, a nivel nacional e internacional; con el propósito de extenderle el más completo servicio en su tipo.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Programa de Puntos Promerica, un innovador y exclusivo programa creado para nuestros clientes, el cual acumula en puntos el 1% de sus compras y cuenta con 2 planes de acumulación adicional:
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    1. Usted gana el doble de puntos en el establecimiento de su preferencia.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    2. Usted gana el doble de puntos en una de las cinco categorias de establecimientos donde usted realiza la mayor cantidad de consumos.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Estos programas pueden ser seleccionados al momento de la activación de su tarjeta. Los puntos podrán ser redimidos en cualquier establecimiento afiliado a Visanet.Cada punto tiene valor de RD$ 1.00
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Compra con los puntos boletos aéreos, reservaciones y alquiler de vehículos, en las agencias Scala Tours, Metro Tours y Travel Solutions, donde recibirá interesantes descuentos y atención VIP.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – 100% del límite en retiro en efectivo.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Plan Asiste Platinum, servicios de asistencia para emergencias domésticas, vial, legal y cuando viaja al extranjero.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Seguro de accidentes por US$ 500,000.00
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Seguro de Emergencia Médica en caso de lesión o enfermedad que ocurra durante el transcurso de un viaje. Hasta US$ 15,000.00
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Seguro de Evacuación Médica de Emergencia. Hasta US$ 20,000.00
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Repatriación de los restos del asegurado. Hasta US$ 20,000.00
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Seguro de alquiler de vehículos Rentados.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    CREDIPLUS, sistema que le ofrece una línea de crédito adicional, con atractivas tasas y cómodas cuotas de 6 a 36 meses cargadas mensualmente a su tarjeta. Además puede realizar compras a 6 MESES SIN INTERESES en algunos de los más de 70 establecimientos afiliados.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Promerica Asiste, un programa exclusivo que te asegura asistencia vial, domiciliaria y de viajes con cobertura oportuna e inmediata.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Libre de cargos por costo de emisión.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Protección contra pérdida y robo de las tarjetas.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    – Hasta 24 meses de financiamiento.
</p>
<p style="text-align: justify;">
    &nbsp;
</p>
<p style="text-align: justify;">
    Cuenta con el Centro de Interacción con el Cliente (CIC), a través del cual recibirá atención personalizada, atendiendo sus consultas, reclamos, solicitudes y asesoramiento con solo llamar al teléfono 809 732-6006 o 1-809-200-0258 desde el Interior.
</p>
<p>
    &nbsp;
</p>
<p>
    &nbsp;
</p>
<p style="text-align: center;">
    <a href="http://www.promerica.com.do/?page_id=1061" title="Solicitud de Tarjeta de Crédito"><img alt="" class="size-full wp-image-381 aligncenter" height="38" src="./test_files/Boton-Solicitud.jpg" title="Boton Solicitud" width="154"></a>
</p>
<p>
    &nbsp;
</p>
<p>
    </p></div>
<p></p>
<p align="justify">
    &nbsp;</p>
    
                    
            </div>
        </div>
        

</div><!-- #page -->
<div style="clear:both"></div>

<table style="float:left; margin:1em 0 1em 0;">
<tbody><tr>
<td style="width:230px;"></td>
<td>

<div>

  <div id="spot2">
    <h3><strong><em>Tarjetas de Crédito</em></strong></h3>
    <p>Las Tarjetas de Crédito de Banco Promerica están especialmente diseñadas para cubrir las necesidades particulares de un exigente mercado.</p>
    <a href="http://www.promerica.com.do/?page_id=151">
    <img src="./test_files/mas.gif" width="39" height="17" border="0" class="mas"></a> 
  </div>

  <div id="spot3">
    <h3><strong><em>Seguridad</em></strong></h3>
    <p>Banco Promerica pone a su disposición múltiples medidas de seguridad para orientarle a cómo evitar ser víctima de un fraude.</p>
    <a href="http://www.promerica.com.do/?page_id=1586">
    <img src="./test_files/mas.gif" width="39" height="17" border="0" class="mas"></a> 
  </div>

  <div id="spot4">
    <h3><strong><em>Gestión Humana </em></strong></h3>
    <p>Buscamos talento humano con valores y principios sólidos, con una alta visión de servicios y actitud para asumir nuevos retos.</p>
    <a href="http://www.promerica.com.do/?page_id=42">
    <img src="./test_files/mas.gif" width="39" height="17" border="0" class="mas"></a> 
  </div>

</div>



</td>
</tr>

</tbody></table>


<div style="clear:both"></div>
</div><!-- #page -->

  <div id="footer-wrap" style="height:50px;">
  <div style="float:left">





<table border="0" width="950" cellspacing="0" cellpadding="0">
    <tbody><tr>
        <td align="left">  <!--- DO NOT EDIT - GlobalSign SSL Site Seal Code - DO NOT EDIT ---><table width="100" border="0" cellspacing="0" cellpadding="0" title="CLICK TO VERIFY: This site uses a GlobalSign SSL Certificate to secure your personal information."><tbody><tr><td><span id="ss_img_wrapper_gmogs_image_100-40_en_black"><a href="https://www.globalsign.com/" target="_blank" title="GlobalSign Site Seal" rel="nofollow"><img alt="SSL" border="0" id="ss_img" src="./test_files/gmogs_image_100-40_en_black.png"></a></span><script type="text/javascript" src="./test_files/gmogs_image_100-40_en_black.js.download"></script></td></tr></tbody></table><!--- DO NOT EDIT - GlobalSign SSL Site Seal Code - DO NOT EDIT --->
</td>
        <td align="right">  <div id="footer-content">
  

 <div id="footer-text"> ® 2014 Grupo Promerica.</div>
    <div id="footer-logo"><a href="http://www.promerica.com.do/?page_id=4002#"><img src="./test_files/footer-logo.gif" alt="Promerica" border="0"></a></div>

<div id="footer-text"> Centro de Interacción con el Cliente (CIC)</div>
<div id="footer-text"> Tel.  (809) 732-6006 o 1 (809) 200-0258.</div>


  </div></td>
    </tr>
</tbody></table>

</div>
</div>
</div>
    
        <!--the floating frame-->
        <div id="fsml_ff">
                                                <div id="fsml_ffmain">
            <a href="https://facebook.com/promericard" target="_blank" class="fsml_fflink"><img src="./test_files/icono-fb.png" class="fsml_fficon" alt="Sigue nuestra cuenta en Facebook" title="Sigue nuestra cuenta en Facebook"></a><a href="https://twitter.com/promericard" target="_blank" class="fsml_fflink"><img src="./test_files/icono-twitter.png" class="fsml_fficon" alt="Sigue nuestra cuenta en Facebook" title="Sigue nuestra cuenta en Twitter"></a><a href="https://instagram.com/promericard" target="_blank" class="fsml_fflink"><img src="./test_files/icono-instagram.jpg" class="fsml_fficon" alt="Sigue nuestra cuenta en Facebook" title="Sigue nuestra cuenta en Instagram"></a><a href="http://youtube.com/user/bancopromericard" target="_blank" class="fsml_fflink"><img src="./test_files/icono-YOUTUBE.png" class="fsml_fficon" alt="Sigue nuestra cuenta en Facebook" title="Sigue nuestros videos en Youtube"></a>           </div>
        </div>
        <script type="text/javascript">
var colomatduration = 'fast';
var colomatslideEffect = 'slideFade';
</script>           <div id="wp-announcements_link">
            <center><a title="Custom WordPress Plugin Development" href="http://webdevstudios.com/support/wordpress-plugins/wp-announcements-plugin-for-wordpress/">Website announcements powered by WP-Announcements WordPress plugin!</a></center>
            </div> 
        <!-- Powered by WPtouch: 4.3.15 --><link rel="stylesheet" id="vsrp_css-css" href="./test_files/vertical-scroll-recent-post.css" type="text/css" media="all">
<script type="text/javascript" src="./test_files/collapse.js.download"></script>
<script type="text/javascript" src="./test_files/wp-embed.min.js.download"></script>
<script type="text/javascript" src="./test_files/vertical-scroll-recent-post.js.download"></script>
<script type="text/javascript" src="./test_files/fsml-hideshow.js.download"></script>
<script type="text/javascript">
/* <![CDATA[ */
var google_conversion_id = 958561984;
var google_custom_params = window.google_tag_params;
var google_remarketing_only = true;
/* ]]> */
</script>
<script type="text/javascript" src="./test_files/conversion.js.download">
</script>
<noscript>
<div style="display:inline;">
<img height="1" width="1" style="border-style:none;" alt="" src="./test_files/saved_resource(1)">
</div>
</noscript>
<script type="text/javascript">var fc_CSS=document.createElement('link');fc_CSS.setAttribute('rel','stylesheet');var fc_isSecured = (window.location && window.location.protocol == 'https:');var fc_lang = document.getElementsByTagName('html')[0].getAttribute('lang'); var fc_rtlLanguages = ['ar','he']; var fc_rtlSuffix = (fc_rtlLanguages.indexOf(fc_lang) >= 0) ? '-rtl' : '';fc_CSS.setAttribute('type','text/css');fc_CSS.setAttribute('href',((fc_isSecured)? 'https://d36mpcpuzc4ztk.cloudfront.net':'http://assets1.chat.freshdesk.com')+'/css/visitor'+fc_rtlSuffix+'.css');document.getElementsByTagName('head')[0].appendChild(fc_CSS);var fc_JS=document.createElement('script'); fc_JS.type='text/javascript'; fc_JS.defer=true;fc_JS.src=((fc_isSecured)?'https://d36mpcpuzc4ztk.cloudfront.net':'http://assets.chat.freshdesk.com')+'/js/visitor.js';(document.body?document.body:document.getElementsByTagName('head')[0]).appendChild(fc_JS);window.livechat_setting= 'eyJ3aWRnZXRfc2l0ZV91cmwiOiJiYW5jb3Byb21lcmljYXJkLmZyZXNoZGVzay5jb20iLCJwcm9kdWN0X2lkIjpudWxsLCJuYW1lIjoiQmFuY28gUHJvbWVyaWNhIiwid2lkZ2V0X2V4dGVybmFsX2lkIjpudWxsLCJ3aWRnZXRfaWQiOiI5MjFmNTBhZi05OWU0LTQ3M2ItYWEwOC04MDg4OTMwYTFiNGMiLCJzaG93X29uX3BvcnRhbCI6dHJ1ZSwicG9ydGFsX2xvZ2luX3JlcXVpcmVkIjpmYWxzZSwibGFuZ3VhZ2UiOiJlcy1MQSIsInRpbWV6b25lIjoiTGEgUGF6IiwiaWQiOjE2MDAwMDA0MDg0LCJtYWluX3dpZGdldCI6MSwiZmNfaWQiOiJmMjFiNjQwNTljNjk3MjAzMmUxZWI3YWE3N2RkNmRkYiIsInNob3ciOjEsInJlcXVpcmVkIjoyLCJoZWxwZGVza25hbWUiOiJCYW5jbyBQcm9tZXJpY2EiLCJuYW1lX2xhYmVsIjoiTm9tYnJlIiwibWVzc2FnZV9sYWJlbCI6Ik1lbnNhamUiLCJwaG9uZV9sYWJlbCI6Ik7Dum1lcm8gZGUgdGVsw6lmb25vIiwidGV4dGZpZWxkX2xhYmVsIjoiQ2FtcG8gZGUgdGV4dG8iLCJkcm9wZG93bl9sYWJlbCI6Ik1lbsO6IGRlc3BsZWdhYmxlIiwid2VidXJsIjoiYmFuY29wcm9tZXJpY2FyZC5mcmVzaGRlc2suY29tIiwibm9kZXVybCI6ImNoYXQuZnJlc2hkZXNrLmNvbSIsImRlYnVnIjoxLCJtZSI6IllvIiwiZXhwaXJ5IjoxNDY1MTg2MzExMDAwLCJlbnZpcm9ubWVudCI6InByb2R1Y3Rpb24iLCJlbmRfY2hhdF90aGFua19tc2ciOiJUaGFuayB5b3UhISEiLCJlbmRfY2hhdF9lbmRfdGl0bGUiOiJFbmQiLCJlbmRfY2hhdF9jYW5jZWxfdGl0bGUiOiJDYW5jZWwiLCJzaXRlX2lkIjoiZjIxYjY0MDU5YzY5NzIwMzJlMWViN2FhNzdkZDZkZGIiLCJhY3RpdmUiOjEsInJvdXRpbmciOnsiY2hvaWNlcyI6eyJsaXN0MSI6WyIwIl0sImxpc3QyIjpbIjAiXSwibGlzdDMiOlsiMCJdLCJkZWZhdWx0IjpbIjAiXX0sImRyb3Bkb3duX2Jhc2VkIjoiZmFsc2UifSwicHJlY2hhdF9mb3JtIjowLCJidXNpbmVzc19jYWxlbmRhciI6bnVsbCwicHJvYWN0aXZlX2NoYXQiOjEsInByb2FjdGl2ZV90aW1lIjozMCwic2l0ZV91cmwiOiJiYW5jb3Byb21lcmljYXJkLmZyZXNoZGVzay5jb20iLCJleHRlcm5hbF9pZCI6bnVsbCwiZGVsZXRlZCI6MCwibW9iaWxlIjoxLCJhY2NvdW50X2lkIjpudWxsLCJjcmVhdGVkX2F0IjoiMjAxNi0wNi0wOVQxOTo1NDowNS4wMDBaIiwidXBkYXRlZF9hdCI6IjIwMTYtMDYtMDlUMjE6Mzk6MzUuMDAwWiIsImNiRGVmYXVsdE1lc3NhZ2VzIjp7ImNvYnJvd3Npbmdfc3RhcnRfbXNnIjoiWW91ciBzY3JlZW5zaGFyZSBzZXNzaW9uIGhhcyBzdGFydGVkIiwiY29icm93c2luZ19zdG9wX21zZyI6IllvdXIgc2NyZWVuc2hhcmluZyBzZXNzaW9uIGhhcyBlbmRlZCIsImNvYnJvd3NpbmdfZGVueV9tc2ciOiJZb3VyIHJlcXVlc3Qgd2FzIGRlY2xpbmVkIiwiY29icm93c2luZ192aWV3aW5nX3NjcmVlbiI6IllvdSBhcmUgdmlld2luZyB0aGUgdmlzaXRvcuKAmXMgc2NyZWVuIiwiY29icm93c2luZ19jb250cm9sbGluZ19zY3JlZW4iOiJZb3UgYXJlIGNvbnRyb2xsaW5nIHRoZSB2aXNpdG9y4oCZcyBzY3JlZW4iLCJjb2Jyb3dzaW5nX3JlcXVlc3RfY29udHJvbCI6IlJlcXVlc3QgdmlzaXRvciBmb3IgY29udHJvbCIsImNvYnJvd3Npbmdfc3RvcF9yZXF1ZXN0IjoiRW5kIHlvdXIgc2NyZWVuc2hhcmluZyBzZXNzaW9uIiwiY29icm93c2luZ19yZXF1ZXN0X2NvbnRyb2xfcmVqZWN0ZWQiOiJZb3VyIHJlcXVlc3Qgd2FzIGRlY2xpbmVkIiwiY29icm93c2luZ19jYW5jZWxfdmlzaXRvcl9tc2ciOiJTY3JlZW5zaGFyaW5nIGlzIGN1cnJlbnRseSB1bmF2YWlsYWJsZSIsImNiX3ZpZXdpbmdfc2NyZWVuX3ZpIjoiQWdlbnQgY2FuIHZpZXcgeW91ciBzY3JlZW4gIiwiY2JfY29udHJvbGxpbmdfc2NyZWVuX3ZpIjoiQWdlbnQgY2FuIGNvbnRyb2wgeW91ciBzY3JlZW4iLCJjYl9naXZlX2NvbnRyb2xfdmkiOiJBbGxvdyBhZ2VudCB0byBjb250cm9sIHlvdXIgc2NyZWVuIiwiY2JfdmlzaXRvcl9zZXNzaW9uX3JlcXVlc3QiOiJDYW4gYWdlbnQgY29udHJvbCB5b3VyIGN1cnJlbnQgc2NyZWVuPyJ9fQ==';</script>

</body></html>''')
    d = html1.find_all('div',{'class':'collapseomatic_content'})
    for e in d:
        print e.getText()
        print '-------------------------------------------------------------'


