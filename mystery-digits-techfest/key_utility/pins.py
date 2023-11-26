def write_sorted_list_to_file(sorted_list, filename):
    with open(filename, 'w') as file:
        file.write(str(sorted_list))

def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_item = sorted_list[mid]

        if mid_item == target:
            return mid  # Found the target at index mid
        elif mid_item < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

def search(target_pin):
    # Example 1
    

    sorted_list1=['abfi', 'acde', 'acpt', 'adss', 'aevf', 'afzk', 'agvj', 'ahey', 'alxv', 'anxi', 'apmf', 'aptw', 'auaa', 'avmh', 'baqh', 'bavs', 'bdtn', 'bhdu', 'bktl', 'bmwd', 'bqdi', 'bstd', 'bxny', 'cafw', 'cbfx', 'cdxr', 'cere', 'cfvv', 'cgnm', 'chwm', 'ckfo', 'cksy', 'cnye', 'ctvi', 'cuaf', 'cuwq', 'cuyr', 'cwhj', 'dakc', 'ddtf', 'dfvh', 'djgv', 'dkvh', 'dolx', 'dpgv', 'drqa', 'dsjs', 'dsnw', 'dsyk', 'dtgj', 'dvvb', 'dwds', 'dyoc', 'efdk', 'ejak', 'epqf', 'euae', 'evdn', 'evfo', 'exzk', 'fdol', 'fdqe', 'feur', 'ffvf', 'fgce', 'fiws', 'fkbx', 'fljt', 'fmbx', 'fmys', 'fnzb', 'fokz', 'fslv', 'fynb', 'fyqm', 'fzqw', 'gbdo', 'gdvt', 'gebl', 'gebt', 'gfjr', 'gfyv', 'ggwd', 'girk', 'gjff', 'gjgr', 'gjkj', 'gjxc', 'gkhd', 'gnew', 'gnnf', 'gprd', 'gtto', 'hbop', 'hcko', 'hcrk', 'hfmn', 'hgzk', 'hijh', 'hmwq', 'hnfo', 'hsdf', 'hssh', 'hukh', 'husm', 'huxt', 'hvkz', 'hvvc', 'hwlg', 'hykh', 'ibam', 'iccy', 'imni', 'inmn', 'iqjj', 'irvd', 'ixuk', 'jahm', 'japp', 'jcar', 'jcrg', 'jddf', 'jdnx', 'jhle', 'jnwk', 'joul', 'jqad', 'jrkh', 'jryq', 'jtgm', 'jtol', 'jujq', 'jvqu', 'jwjz', 'jxlt', 'jxvb', 'jzaj', 'kcac', 'kddm', 'kewo', 'kgul', 'kjab', 'kjea', 'kmlk', 'knrn', 'kpjg', 'ktcm', 'kugq', 'ldum', 'lfgd', 'lgpg', 'line', 'ljsc', 'lmjz', 'lnlm', 'lokk', 'lovz', 'lpec', 'lrfs', 'lrsy', 'lwli', 'mari', 'mcbz', 'meak', 'mfsm', 'mhwh', 'mjey', 'mlld', 'mspm', 'msuf', 'muyg', 'nhhn', 'njot', 'njxg', 'nkot', 'nlcu', 'nlis', 'nwsp', 'ocet', 'oclu', 'ojiu', 'ojlj', 'ojul', 'olkv', 'onma', 'ouou', 'ovsw', 'oxzo', 'oybo', 'oyiw', 'ozqj', 'paql', 'piav', 'pigl', 'pmzy', 'pnyq', 'prkm', 'psmd', 'pssx', 'puqj', 'pvsb', 'pvtc', 'qfdi', 'qfny', 'qnii', 'qpkd', 'qrbs', 'qwqo', 'qzcs', 'rasy', 'rczq', 'rdzp', 'rgso', 'rigd', 'rkek', 'rkpz', 'rlbs', 'rltj', 'rrjo', 'rsnq', 'rtkc', 'rupr', 'rykm', 'sbor', 'sbym', 'scul', 'sjsf', 'spjx', 'sqca', 'szpo', 'szul', 'tbds', 'tfky', 'tivn', 'tjoj', 'tmwi', 'tpal', 'tqam', 'tvgu', 'tzyt', 'uapv', 'ucee', 'uoji', 'uoma', 'upsm', 'uqrb', 'usvt', 'utdo', 'vbbn', 'vbth', 'vhfo', 'vhnn', 'vkxn', 'vlzk', 'vngi', 'vvqs', 'vwfi', 'vwhv', 'vxmb', 'wage', 'wbim', 'weff', 'wibd', 'wkmt', 'wpqk', 'wpry', 'wtlr', 'wzzd', 'xblw', 'xedo', 'xgvm', 'xigg', 'xluq', 'xpoe', 'xqkr', 'xrny', 'xywa', 'yava', 'ydbh', 'yegi', 'ygiy', 'yipd', 'yori', 'ysxo', 'ytaj', 'yuva', 'yzjo', 'zcfk', 'zckw', 'zcyn', 'zfyk', 'zhjg', 'zoau', 'zpqv', 'zpvk', 'zpwy', 'zshs', 'zsso', 'zvfc', 'zzxq']
    index = binary_search(sorted_list1, target_pin)

    if index != -1:
        return 1
    else:
        return 0
if __name__ == "__main__":
    main()
