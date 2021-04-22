class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = []

        for addr in emails:
            at = addr.index('@')

            try:
                plus = addr.index('+')
                if plus < at:
                    addr = addr[:plus] + addr[at:]
                    at = plus
            except:
                pass

            while True:
                try:
                    period = addr.index('.')
                    if period < at:
                        addr = addr[:period] + addr[(period + 1):]
                    else:
                        break
                except:
                    break
            ans.append(addr)

        return len(set(ans))