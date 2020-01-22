def pre():
    cucm_device_pools = ['Default', 'site1-dp', 'site2-dp', 'site3-dp']
    cucm_regions = ['Default', 'site1-reg', 'site2-reg', 'site3-reg']

    return locals()

def main(**kwargs):
    print(locals())
    return {'some': 'value'}

if __name__ == "__main__":
    vars = pre()
    main(**vars)
